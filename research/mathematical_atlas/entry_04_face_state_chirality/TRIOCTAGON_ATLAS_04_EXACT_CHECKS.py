"""Atlas 04: independent exact face-state algebra and separate runtime checks.

Run with conda environment torment and -B. Output must be outside protected trees.
Reference algebra is constructed from Atlas-03 affine panel maps, without kernel
imports. Only API/ownership/precision groups import the current implementation.
Optional --integrity-dir attaches pre-captured full before/after inventories.
No source writes, commits, pushes, plot caches, or bytecode files are produced.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

sys.dont_write_bytecode = True
import sympy as s

REPO = Path(r'C:\TORMENT\TRIOCTAGON_new\trioctagon-physics')
OLD = Path(r'C:\TORMENT\TRIOCTAGON_new\kernel_TO')
PROD = Path(r'C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric')
BASELINE = '0fa3b582c086e51371e8a784bc3dd145f88cfb2b'
SOURCES = {
    'B_CODE': REPO/'kernel_physics/face_state.py',
    'READOUTS': REPO/'kernel_physics/readouts.py',
    'B_PAPER': REPO/'papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md',
    'B_SYMBOLS': REPO/'papers/PAPER_B/PAPER_B_SYMBOLS_AND_THEOREMS_v0.1.1.md',
    'GEOMETRY': REPO/'kernel_physics/geometry.py',
    'DYNAMICS': REPO/'kernel_physics/dynamics.py',
    'NUMERIC_POLICY': REPO/'kernel_physics/_response_numeric.py',
    'BOUNDED_WRAPPER': REPO/'kernel_physics/operating_region.py',
    'FACE_TESTS': REPO/'kernel_physics/tests/test_face_state.py',
    'READOUT_TESTS': REPO/'kernel_physics/tests/test_readouts.py',
    'OLD_MODEL': OLD/'model_core.py',
    'OLD_3D': OLD/'geometry_3d.py',
    'OLD_TETRA': OLD/'dual_tetra_mapper.py',
    'OLD_CURVES': OLD/'analysis_tools.py',
    'OLD_CORRIDOR': OLD/'tangent_corridor_analysis.py',
    'PRODUCTION_MODEL': PROD/'torment_service/kernel/model_core.py',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def simp(x):
    return s.simplify(s.trigsimp(s.expand(x)))


def eq(a, b):
    if isinstance(a, s.MatrixBase) or isinstance(b, s.MatrixBase):
        a, b = s.Matrix(a), s.Matrix(b)
        return a.shape == b.shape and all(simp(x-y)==0 for x,y in zip(a,b))
    return simp(a-b)==0


def cross_matrix(n):
    return s.Matrix([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])


def serial(x):
    if isinstance(x,s.MatrixBase): return [[serial(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
    if isinstance(x,s.Basic): return str(x)
    if isinstance(x,dict): return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [serial(v) for v in x]
    return x


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--integrity-dir',type=Path)
    args=parser.parse_args()
    target=args.output.resolve()
    if any(target==p.resolve() or p.resolve() in target.parents for p in (REPO,OLD,PROD)):
        raise SystemExit('Output may not be inside a protected tree')
    sources={name:{'path':str(p),'sha256':sha(p)} for name,p in SOURCES.items()}
    checks=[]
    def check(group,name,condition,evidence=None):
        ok=bool(condition)
        checks.append({'group':group,'name':name,'passed':ok,'evidence':serial(evidence)})
        if not ok: print('FAIL',group,name,flush=True)
    VEC=s.Matrix; I=s.eye(3); ez=VEC([0,0,1]); half=s.Rational(1,2)
    u,z=s.symbols('u z',real=True)
    maps=[VEC([-s.Rational(1,4)-u/2,s.sqrt(3)/4-s.sqrt(3)*u/2,z]),
          VEC([u,0,z]),VEC([s.Rational(1,4)-u/2,s.sqrt(3)/4+s.sqrt(3)*u/2,z])]
    centres=[p.subs({u:0,z:0}) for p in maps]
    normals=[p.diff(u).cross(p.diff(z)) for p in maps]
    tangents=[ez.cross(n) for n in normals]
    B=[s.Matrix.hstack(t,ez) for t in tangents]
    Pi=[b*b.T for b in B]
    J=[cross_matrix(n) for n in normals]
    T={(i,j):B[i]*B[j].T for i in range(3) for j in range(3)}
    q=VEC(s.symbols('q0:3',real=True)); p=VEC(s.symbols('p0:3',real=True))
    w=q+s.I*p
    vectors=[B[i]*VEC([q[i],p[i]]) for i in range(3)]
    def encode(i,v): return tangents[i].dot(v)+s.I*ez.dot(v)
    def decode(i,c): return B[i]*VEC([s.re(c).expand(complex=True),s.im(c).expand(complex=True)])
    check('EXACT_ALGEBRA','frames_inherited_from_affine_panel_derivatives',all(eq(t,m.diff(u)) and eq(s.Matrix.hstack(t,ez,n).T*s.Matrix.hstack(t,ez,n),I) and eq(s.Matrix.hstack(t,ez,n).det(),1) for t,n,m in zip(tangents,normals,maps)),{'centres':centres,'normals':normals,'tangents':tangents})
    check('EXACT_ALGEBRA','all_tangent_projectors',all(eq(Pi[i],I-normals[i]*normals[i].T) and eq(Pi[i]**2,Pi[i]) and Pi[i].rank()==2 and eq(Pi[i]*normals[i],s.zeros(3,1)) for i in range(3)))
    a,b,c,d=s.symbols('a b c d',real=True)
    v1=VEC([a,b]); v2=VEC([c,d]); rho,sigma=s.symbols('rho sigma',real=True)
    check('EXACT_ALGEBRA','real_linearity_norm_and_inner_product',all(eq(Bi*(rho*v1+sigma*v2),rho*(Bi*v1)+sigma*(Bi*v2)) and eq((Bi*v1).dot(Bi*v2),a*c+b*d) and eq((Bi*v1).dot(Bi*v1),a*a+b*b) for Bi in B))
    bigB=s.diag(*B)
    check('EXACT_ALGEBRA','product_real_isometry_6_to_9',bigB.shape==(9,6) and bigB.rank()==6 and eq(bigB.T*bigB,s.eye(6)) and eq(bigB*bigB.T,s.diag(*Pi)))
    ambient=VEC(s.symbols('X Y Z',real=True))
    check('EXACT_ALGEBRA','ED_identity_and_DE_ambient_projection',all(eq(encode(i,vectors[i]),w[i]) and eq(decode(i,encode(i,ambient)),Pi[i]*ambient) for i in range(3)))
    check('EXACT_ALGEBRA','image_exact_tangent_plane_certificate',all(B[i].rank()==2 and eq(normals[i].T*B[i],s.zeros(1,2)) and eq(B[i]*B[i].T+normals[i]*normals[i].T,I) for i in range(3)))
    J2=s.Matrix([[0,-1],[1,0]]); K=-J2
    check('EXACT_ALGEBRA','complex_structure_tangent_and_ambient_domains',all(eq(J[i]*tangents[i],ez) and eq(J[i]*ez,-tangents[i]) and eq(J[i]**2,-Pi[i]) and eq(J[i]*B[i],B[i]*J2) and eq(decode(i,s.I*w[i]),J[i]*vectors[i]) for i in range(3)))
    check('EXACT_ALGEBRA','area_form_sign_and_compatibility',all(eq(normals[i].dot((B[i]*v1).cross(B[i]*v2)),a*d-b*c) and eq((J[i]*B[i]*v1).dot(B[i]*v2),a*d-b*c) and eq(normals[i].dot((B[i]*v1).cross(J[i]*B[i]*v2)),v1.dot(v2)) and eq(B[i].T*(-J[i])*B[i],K) for i in range(3)),{'J_coordinate_matrix':J2,'area_form_matrix':K})
    check('EXACT_ALGEBRA','area_form_matches_imaginary_Hermitian_product',eq(s.im(s.conjugate(a+s.I*b)*(c+s.I*d)),a*d-b*c))
    check('EXACT_ALGEBRA','all_nine_transport_component_rank_kernel_image_identities',all(eq(T[i,j]*B[j],B[i]) and T[i,j].rank()==2 and eq(T[i,j]*normals[j],s.zeros(3,1)) and eq(normals[i].T*T[i,j],s.zeros(1,3)) for i,j in T))
    check('EXACT_ALGEBRA','all_27_ambient_transport_compositions',all(eq(T[i,j]*T[j,k],T[i,k]) for i,j,k in itertools.product(range(3),repeat=3)))
    check('EXACT_ALGEBRA','transport_partial_isometry_and_adjoint',all(eq(T[i,j].T,T[j,i]) and eq(T[i,j].T*T[i,j],Pi[j]) and eq(T[i,j]*T[i,j].T,Pi[i]) for i,j in T))
    R=s.Matrix([[-half,-s.sqrt(3)/2,0],[s.sqrt(3)/2,-half,0],[0,0,1]])
    V=s.diag(-1,1,1); H=s.diag(1,1,-1); origin=VEC([0,s.sqrt(3)/6,0])
    check('EXACT_ALGEBRA','transport_equals_projected_matched_C3_rotation',all(eq(T[i,j],Pi[i]*R**((i-j)%3)) and eq(T[i,j],R**((i-j)%3)*Pi[j]) and eq(R**((i-j)%3),T[i,j]+normals[i]*normals[j].T) for i,j in T))
    check('EXACT_ALGEBRA','point_affine_rotation_and_free_vector_transport',all(eq(origin+R*(centres[i]+vectors[i]-origin),centres[(i+1)%3]+T[(i+1)%3,i]*vectors[i]) for i in range(3)))
    hol=T[0,2]*T[2,1]*T[1,0]
    check('EXACT_ALGEBRA','A_B_C_A_holonomy_identity_on_tangent_only',eq(hol,Pi[0]) and eq(hol*B[0],B[0]) and not eq(hol,I),hol)
    theta_i,theta_j,theta_k=s.symbols('theta_i theta_j theta_k',real=True)
    rot2=lambda t:s.Matrix([[s.cos(t),-s.sin(t)],[s.sin(t),s.cos(t)]])
    check('EXACT_ALGEBRA','passive_frame_coordinate_transport',eq(rot2(theta_i).T*rot2(theta_j),rot2(theta_j-theta_i)) and eq((theta_j-theta_i)+(theta_k-theta_j)+(theta_i-theta_k),0))

    eps,g,delta=s.symbols('eps g delta',real=True); kval=s.symbols('k0:3',real=True)
    L=s.ones(3)-3*I
    precomplex=w+eps*VEC([w[i]*(kval[i]-q[i]**2-p[i]**2) for i in range(3)])+g*L*w
    prefaces=[vectors[i]+eps*(kval[i]-vectors[i].dot(vectors[i]))*vectors[i]+g*sum((T[i,j]*vectors[j]-vectors[i] for j in range(3) if j!=i),s.zeros(3,1)) for i in range(3)]
    check('EXACT_ALGEBRA','symbolic_cubic_and_coupling_coordinate_conjugacy',all(eq(encode(i,prefaces[i]),precomplex[i]) for i in range(3)))
    check('EXACT_ALGEBRA','phase_step_outward_J_rotation_dictionary',all(eq(encode(i,s.cos(delta)*vectors[i]+s.sin(delta)*J[i]*vectors[i]),(s.cos(delta)+s.I*s.sin(delta))*w[i]) for i in range(3)))
    check('EXACT_ALGEBRA','zero_rotations_remain_zero',all(eq((s.cos(delta)*I+s.sin(delta)*J[i])*s.zeros(3,1),s.zeros(3,1)) for i in range(3)))
    # Exact zero-stratum witness for synchronizer, eps=g=0, alpha=lambda=pi/6.
    alpha0=s.pi/6; lam0=s.pi/6
    oldphase=[s.Integer(0)]*3; shiftedphase=[s.Integer(0),alpha0,alpha0]
    inc=lambda phases,i:lam0*sum(s.sin(3*(phases[j]-phases[i])) for j in range(3) if i!=j)
    check('EXACT_FALSIFIER','common_phase_not_global_recurrence_symmetry_at_zero',eq(inc(oldphase,1),0) and eq(inc(shiftedphase,1),-lam0) and eq(alpha0+inc(shiftedphase,1),0) and not eq(s.cos(alpha0)+s.I*s.sin(alpha0),1),{'state':[0,1,1],'phase_shift':alpha0,'lambda':lam0,'nonzero_output_after_shift':'1','phase_times_original_output':s.cos(alpha0)+s.I*s.sin(alpha0)})

    area=s.Matrix(3,3,lambda i,j:simp(normals[i].dot(vectors[i].cross(T[i,j]*vectors[j]))))
    Z=q.cross(p)
    check('EXACT_ALGEBRA','all_nine_transported_areas_direct_geometry',eq(area,q*p.T-p*q.T) and all(eq(area[i,j],s.im(s.conjugate(w[i])*w[j])) for i,j in itertools.product(range(3),repeat=2)),area)
    check('EXACT_ALGEBRA','area_skew_zero_diagonal_raw_cyclic_chirality',eq(area.T,-area) and all(area[i,i]==0 for i in range(3)) and eq(VEC([area[1,2],area[2,0],area[0,1]]),Z) and eq(area,-cross_matrix(Z)),Z)
    normZ=Z.dot(Z)
    spectral=s.Symbol('lambda_spectral')
    check('EXACT_ALGEBRA','area_trace_determinant_Gram_and_Frobenius_invariants',eq(s.trace(area),0) and eq(area.det(),0) and eq(normZ,q.dot(q)*p.dot(p)-q.dot(p)**2) and eq(s.trace(area.T*area),2*normZ))
    check('EXACT_ALGEBRA','area_square_cube_kernel_and_characteristic_polynomial',eq(area*Z,s.zeros(3,1)) and eq(area**2,Z*Z.T-normZ*I) and eq(area**3,-normZ*area) and eq(area.charpoly(spectral).as_expr(),spectral*(spectral**2+normZ)))
    witness_sub={q[0]:0,q[1]:1,q[2]:0,p[0]:0,p[1]:0,p[2]:1}
    check('EXACT_ALGEBRA','rank_two_and_zero_rank_witnesses',area.subs(witness_sub).rank()==2 and area.subs({p[i]:2*q[i] for i in range(3)}).rank()==0 and eq((VEC([1,-2,3])).cross(s.zeros(3,1)),s.zeros(3,1)))
    alpha=s.symbols('alpha',real=True)
    qp=s.cos(alpha)*q-s.sin(alpha)*p; pp=s.sin(alpha)*q+s.cos(alpha)*p
    check('EXACT_ALGEBRA','global_phase_vectors_and_area_chirality_invariance',all(eq(B[i]*VEC([qp[i],pp[i]]),s.cos(alpha)*vectors[i]+s.sin(alpha)*J[i]*vectors[i]) for i in range(3)) and eq(qp*pp.T-pp*qp.T,area) and eq(qp.cross(pp),Z))
    check('EXACT_ALGEBRA','raw_complex_scaling_and_conjugation',eq((a*q-b*p).cross(b*q+a*p),(a*a+b*b)*Z) and eq(q.cross(-p),-Z) and eq(q*(-p).T-(-p)*q.T,-area))

    group=[]
    for r,v,h in itertools.product(range(3),range(2),range(2)):
        G=R**r*V**v*H**h
        perm=[next(j for j in range(3) if eq(G*normals[i],normals[j])) for i in range(3)]
        P=s.zeros(3)
        for i,j in enumerate(perm):P[j,i]=1
        detG,detP,eta=G.det(),P.det(),(G*ez)[2]
        transformed=[s.zeros(3,1) for _ in range(3)]
        for i,j in enumerate(perm):transformed[j]=G*vectors[i]
        encoded=VEC([simp(encode(i,transformed[i])) for i in range(3)])
        expected=eta*P*w if detG==1 else -eta*P*s.conjugate(w)
        area_prime=s.Matrix(3,3,lambda i,j:simp(normals[i].dot(transformed[i].cross(T[i,j]*transformed[j]))))
        Zprime=VEC([area_prime[1,2],area_prime[2,0],area_prime[0,1]])
        check('EXACT_SPATIAL_ACTION',f'R{r}_V{v}_H{h}_frame_transport_state_area_Z_laws',all(eq(G*tangents[i],detG*eta*tangents[perm[i]]) and eq(origin+G*(centres[i]-origin),centres[perm[i]]) for i in range(3)) and all(eq(G*T[i,j]*G.T,T[perm[i],perm[j]]) for i,j in T) and eq(encoded,expected) and eq(area_prime,detG*P*area*P.T) and eq(Zprime,detG*detP*P*Z))
        group.append({'element':f'R^{r} V^{v} H^{h}','G':G,'source_to_destination':perm,'P':P,'det_G':detG,'det_P':detP,'eta':eta,'state_action':'eta P Omega' if detG==1 else '-eta P conjugate(Omega)','Z_matrix':detG*detP*P})
    pure=[]
    for perm in itertools.permutations(range(3)):
        P=I[list(perm),:]
        condition=eq((P*q)*(P*p).T-(P*p)*(P*q).T,P*area*P.T) and eq((P*q).cross(P*p),P.det()*P*Z)
        pure.append(condition)
    check('EXACT_ALGEBRA','all_six_pure_channel_relabellings',all(pure))
    Pcyc=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    Zw=Z.subs(witness_sub); channel=Pcyc*Zw; spatial=R*Zw
    check('EXACT_FALSIFIER','cyclic_witness_channel_triple_not_ambient_axial_vector',eq(Zw,VEC([1,0,0])) and eq(channel,VEC([0,1,0])) and eq(spatial,VEC([-half,s.sqrt(3)/2,0])) and eq((channel-spatial).dot(channel-spatial),2-s.sqrt(3)) and not eq(channel,spatial),{'Omega':[0,1,s.I],'Z':Zw,'PZ':channel,'RZ':spatial,'squared_gap':2-s.sqrt(3)})
    check('EXACT_FALSIFIER','transport_is_not_invertible_ambient_rotation',all(T[i,j].det()==0 and not eq(T[i,j].T*T[i,j],I) and not eq(T[i,j]*normals[j],R**((i-j)%3)*normals[j]) for i,j in T))
    check('EXACT_FALSIFIER','ambient_inverse_requires_projection',all(eq(decode(i,encode(i,vectors[i]+normals[i])),vectors[i]) and not eq(vectors[i]+normals[i],vectors[i]) for i in range(3)))
    check('EXACT_FALSIFIER','normals_not_a_Cartesian_basis',s.Matrix.hstack(*normals).rank()==2 and eq(sum(normals,s.zeros(3,1)),s.zeros(3,1)) and eq(normals[0].dot(normals[1]),-half))
    check('EXACT_FALSIFIER','decoding_has_no_polygon_endpoint_bound',eq(decode(1,s.Integer(10)),VEC([10,0,0])) and decode(1,s.Integer(10))[0]>half)
    check('EXACT_FALSIFIER','transporting_centres_is_not_point_rotation',not eq(T[2,1]*centres[1],centres[2]) and eq(origin+R*(centres[1]-origin),centres[2]))

    # Separate finite-precision/API lane; imports cannot contribute to proofs above.
    sys.path.insert(0,str(REPO))
    import numpy as np
    from unittest.mock import patch
    from kernel_physics import face_state as fs, dynamics as dy, readouts, geometry, operating_region as region
    from kernel_physics._response_numeric import ResponsePrecisionError
    def arr(x):return np.array(x,dtype=float)
    def close(x,y):return np.allclose(x,y,rtol=4e-15,atol=4e-16)
    def raises(fn,types):
        try:fn()
        except types:return True
        return False
    frames=fs.face_frames()
    check('API_FLOAT','loaded_authoritative_modules_and_exact_frame_tuples',Path(fs.__file__).resolve()==SOURCES['B_CODE'].resolve() and all(eq(VEC(fs._NORMALS[i]),normals[i]) and eq(VEC(fs._CENTRES[i]),centres[i]) and eq(VEC(fs._TANGENTS[i]),tangents[i]) for i in range(3)))
    check('API_FLOAT','fresh_readonly_frame_arrays_and_convention_metadata',frames.face_order==('A=P1','B=P2','C=P3') and frames.frame_id=='face_center_tangent_ez_v1' and frames.transport_id=='c3_matched_zero_phase_v1' and frames.geometry_sha256==sha(SOURCES['GEOMETRY']) and all(not getattr(frames,k).flags.writeable and not np.shares_memory(getattr(frames,k),getattr(fs.face_frames(),k)) for k in ('centres','normals','tangents','ez')))
    omega=np.array([.6+.2j,-.3+.4j,.15-.9j]); saved=omega.tobytes(); faces=fs.decode_to_faces(omega)
    expected=np.array([arr(B[i]).dot([omega[i].real,omega[i].imag]) for i in range(3)])
    check('API_FLOAT','decoding_roundtrip_and_raw_scale',close(faces,expected) and close(fs.encode_from_faces(faces),omega) and close(fs.encode_from_faces(fs.decode_to_faces(1e-250*omega))/1e-250,omega) and omega.tobytes()==saved and np.linalg.norm(fs.decode_to_faces([10,0,0])[0])>9.9)
    check('API_FLOAT','all_nine_transport_matrices',all(close(fs.transport(i,j),arr(T[i,j])) and not fs.transport(i,j).flags.writeable for i,j in T))
    exact_omega=VEC([1+4*s.I,2+5*s.I,3+6*s.I]); exact_Z=VEC([1,2,3]).cross(VEC([4,5,6]))
    check('API_FLOAT','raw_readout_against_independent_integer_example',np.array_equal(readouts.z_chiral([1+4j,2+5j,3+6j]),arr(exact_Z).ravel()),{'Omega':exact_omega,'Z':exact_Z})
    geometric=np.array([[frames.normals[i].dot(np.cross(faces[i],fs.transport(i,j)@faces[j])) for j in range(3)] for i in range(3)])
    observed=np.array([[fs.state_area(i,j,omega) for j in range(3)] for i in range(3)])
    check('API_FLOAT','all_state_areas_against_geometric_calculation',close(geometric,observed) and np.array_equal(observed.T,-observed))
    with patch.object(readouts,'z_chiral',wraps=readouts.z_chiral) as call:
        delegated=fs.area_triple(omega)
        delegated_once=call.call_count==1
    check('API_OWNERSHIP','area_triple_delegates_bitwise_once',delegated_once and delegated.tobytes()==readouts.z_chiral(omega).tobytes())
    round_state=np.array([1+0j,0j,0j]); rounded=fs.encode_from_faces(fs.decode_to_faces(round_state))
    check('API_FLOAT_FALSIFIER','floating_ED_not_bitwise_identity_witness',rounded.tobytes()!=round_state.tobytes() and close(rounded,round_state),{'initial_real_hex':[z.real.hex() for z in round_state],'roundtrip_real_hex':[z.real.hex() for z in rounded]})
    normal_rejections=[]
    for i,scale in itertools.product(range(3),(1.,1e-250)):
        ambient_array=np.zeros((3,3));ambient_array[i]=scale*frames.normals[i]
        normal_rejections.append(raises(lambda:fs.encode_from_faces(ambient_array),ValueError))
    high_z=fs.decode_to_faces([1,1+1e100j,1]);high_z[1,1]=1e-250
    check('API_PRECISION','normal_rejection_scale_homogeneity_and_no_z_slack',all(normal_rejections) and raises(lambda:fs.encode_from_faces(high_z),ValueError))
    check('API_PRECISION','subnormal_overflow_and_diagonal_readout_validation',raises(lambda:fs.decode_to_faces([1e-320,0,0]),ResponsePrecisionError) and raises(lambda:fs.encode_from_faces([[0,0,1e-320],[0,0,0],[0,0,0]]),ResponsePrecisionError) and raises(lambda:readouts.z_chiral(1e200*omega),ResponsePrecisionError) and raises(lambda:fs.state_area(0,0,1e-170*omega),ResponsePrecisionError))
    tiny=readouts.z_chiral(1e-140*omega)
    check('API_PRECISION','small_nonzero_area_retains_quadratic_scale',np.all(tiny!=0) and close(tiny/1e-280,readouts.z_chiral(omega)))
    check('API_PRECISION','strict_shapes_types_and_indices',all(raises(lambda bad=bad:fs.decode_to_faces(bad),(ValueError,TypeError)) for bad in ([1,2],[True,0,0],['1',0,0],[float('nan'),0,0])) and all(raises(lambda bad=bad:fs.transport(bad,0),(ValueError,TypeError,IndexError)) for bad in (True,1.,'A',-1,3)) and raises(lambda:fs.encode_from_faces(np.zeros((3,3),dtype=complex)),(ValueError,TypeError)))
    view=fs.FaceState(omega);omega_saved=view.omega.tobytes();faces_saved=view.vectors.tobytes()
    check('API_OWNERSHIP','stored_state_copy_and_derived_readonly_vectors',view.omega.tobytes()==omega.tobytes() and np.array_equal(view.vectors,faces) and not np.shares_memory(view.omega,omega) and not view.omega.flags.writeable and not view.vectors.flags.writeable)
    trajectory=[]
    config=region.bounded_config(k=[1,2,3],phase_strength=.01)
    for profile in (None,region.PROFILE_ID):
        cur=fs.FaceState(omega);raw=omega.copy();records=[]
        with patch.object(fs,'encode_from_faces',side_effect=AssertionError('automatic E(D) is forbidden')):
            for index in range(4):
                old_bytes=(cur.omega.tobytes(),cur.vectors.tobytes())
                if profile is None:
                    expected_state=dy.step3(raw,config)
                    with patch.object(dy,'step3',wraps=dy.step3) as call:
                        nxt=cur.step(config)
                        calls=call.call_count
                    adapters=0
                else:
                    expected_state=region.step_bounded_triad(raw,config,profile=profile)
                    with patch.object(region,'step3',wraps=region.step3) as call:
                        with patch.object(region,'step_bounded_triad',wraps=region.step_bounded_triad) as adapter:
                            nxt=cur.step(config,profile=profile)
                            adapters=adapter.call_count
                        calls=call.call_count
                records.append({'step':index+1,'recurrence_calls':calls,'adapter_calls':adapters,'bitwise_equal_to_direct':nxt.omega.tobytes()==expected_state.tobytes(),'previous_view_unchanged':old_bytes==(cur.omega.tobytes(),cur.vectors.tobytes())})
                cur,raw=nxt,expected_state
        trajectory.append({'profile':profile,'records':records})
    check('API_OWNERSHIP','one_recurrence_per_step_no_encode_feedback_both_paths',all(v['recurrence_calls']==1 and v['bitwise_equal_to_direct'] and v['previous_view_unchanged'] and v['adapter_calls']==(0 if branch['profile'] is None else 1) for branch in trajectory for v in branch['records']),trajectory)
    with patch.object(fs,'encode_from_faces',wraps=fs.encode_from_faces) as encoder:
        initialized=fs.FaceState.from_faces(faces)
        count=encoder.call_count
    check('API_OWNERSHIP','from_faces_explicit_single_encoding_initialization',count==1 and initialized.omega.tobytes()==fs.encode_from_faces(faces).tobytes() and np.array_equal(faces,expected))
    with patch.object(dy,'step3',wraps=dy.step3) as stepper:
        with patch.object(fs,'_decode',side_effect=ResponsePrecisionError('test-only injected conversion failure')):
            failed=raises(lambda:view.step(config),ResponsePrecisionError)
        count=stepper.call_count
    check('API_OWNERSHIP','failed_view_conversion_preserves_previous_state',failed and count==1 and view.omega.tobytes()==omega_saved and view.vectors.tobytes()==faces_saved)
    check('API_PRECISION','zero_phase_convention_and_lambda_zero_identity',dy.arg0([complex(-0.,-0.)])[0]==0 and dy.phase_sync(omega,0).tobytes()==omega.tobytes())
    phase=np.exp(1j*np.pi/6);base=np.array([0j,1,1]);config_zero=dy.DynamicsConfig(0,0,np.pi/6,(0,0,0))
    zleft=fs.FaceState(phase*base).step(config_zero).omega;zright=phase*fs.FaceState(base).step(config_zero).omega
    check('API_FLOAT_FALSIFIER','zero_stratum_phase_counterexample',max(abs(zleft-zright))>.5 and close(zleft,base),{'maximum_gap':float(max(abs(zleft-zright)))})

    check('SOURCE_INTEGRITY','consulted_sources_unchanged_during_checks',all(sha(SOURCES[name])==rec['sha256'] for name,rec in sources.items()))
    integrity={'status':'NOT_ATTACHED'}
    if args.integrity_dir:
        before=json.loads((args.integrity_dir/'before.json').read_text(encoding='utf-8'))
        after=json.loads((args.integrity_dir/'after.json').read_text(encoding='utf-8'))
        gb=json.loads((args.integrity_dir/'git_before.json').read_text(encoding='utf-8'))
        integrity={'status':'ATTACHED','scopes':{},'snapshot_paths':{},'snapshot_sha256':{},'git_before':gb,'git_after':{}}
        for name in ('before.json','after.json','git_before.json'):
            path=args.integrity_dir/name;integrity['snapshot_paths'][name]=str(path);integrity['snapshot_sha256'][name]=sha(path)
        for label in ('current','old','torment_kernel','torment_checkout'):
            bfr,aft=before[label],after[label]
            digest=lambda rec:hashlib.sha256(json.dumps(rec['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
            changed=sorted(k for k in set(bfr['files'])|set(aft['files']) if bfr['files'].get(k)!=aft['files'].get(k))
            check('TREE_INTEGRITY',label+'_content_and_paths_unchanged',not changed and bfr['tree_sha256']==digest(bfr)==aft['tree_sha256']==digest(aft))
            integrity['scopes'][label]={'root':bfr['root'],'before_count':bfr['count'],'after_count':aft['count'],'before_sha256':bfr['tree_sha256'],'after_sha256':aft['tree_sha256'],'changed_paths':changed,'before_interval':[bfr['start_utc'],bfr['end_utc']],'after_interval':[aft['start_utc'],aft['end_utc']]}
        for label in ('current','torment_checkout'):
            root=before[label]['root']
            git=lambda *cmd:subprocess.check_output(['git','--no-optional-locks','-C',root,*cmd],text=True).strip()
            ga={'head':git('rev-parse','HEAD'),'tracked_status':git('status','--porcelain','--untracked-files=no')}
            integrity['git_after'][label]=ga
            check('TREE_INTEGRITY',label+'_git_head_and_tracked_status',ga==gb[label] and ga['tracked_status']=='' and (label!='current' or ga['head']==BASELINE))

    summary={'total':len(checks),'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'groups':{g:{'total':sum(c['group']==g for c in checks),'passed':sum(c['group']==g and c['passed'] for c in checks)} for g in sorted({c['group'] for c in checks})}}
    result={'atlas':'04','version':'0.1','generated_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'interpreter':sys.executable,'baseline':BASELINE,'script_path':str(Path(__file__).resolve()),'script_sha256':sha(__file__),'summary':summary,'checks':checks,'sources':sources,'integrity':integrity,'exact_data':{'centres':centres,'normals':normals,'tangents':tangents,'ez':ez,'D_real_matrices':B,'projectors':Pi,'complex_structures':J,'transport':{f'{i}<-{j}':T[i,j] for i,j in T},'A':area,'Z':Z,'holonomy_A':hol,'symmetry_actions':group},'runtime_trajectory_evidence':trajectory,'scope':['Exact algebra is independent of the implementation/API lane.','All normal-bearing ambient inputs have DE=Pi mathematically; production encoder rejects substantive residuals.','Finite runtime cases do not establish bitwise equality for every input or platform.','Historical absence findings are bounded to the inspected files, not proofs about all past work.'],'boundary_flags':['PAPER_C_GEOMETRY != OMEGA_DYNAMICS','OMEGA_HAS_AN_ACCEPTED_TANGENT_VECTOR_REPRESENTATION','NO_ACCEPTED_PHYSICAL_POINT_POSITION_LAW_FROM_OMEGA'],'actions':{'commits':0,'pushes':0}}
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(serial(result),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2));print('OUTPUT',target)
    return int(summary['failed']!=0)


if __name__=='__main__':raise SystemExit(main())
