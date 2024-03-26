import numpy as np


class RayPath:
    def __init__(self):
        pass
    
    def intersection(self, OBJ, p, u):
        x1 = OBJ.x1
        x2 = OBJ.x2
        for i in range(20):
            dx = x2 - x1
            if dx < 1e-12:
                hx = (x1 + x2) / 2
                hy = OBJ.y(hx)
                return np.array([hx, hy]), OBJ.tangent(hx)
            else:
                x = np.linspace(x1, x2, 10)
                y_func = OBJ.y(x)
                V = np.array([x, y_func]) - p.reshape(2,1)
                D = u[0]*V[0] + u[1]*V[1]
                C = u[0]*V[1] - u[1]*V[0]
                hit = (C[:-1] * C[1:] < 0) & (D[:-1]>0) # & (D[1:]>0)
                ind = np.where(hit)[0]
                if len(ind) == 0:
                    return [-1], [-1]
                else:
                    idx = D[ind].argmin()
                    x1 = x[ind[idx]]
                    x2 = x[ind[idx]+1]
    
    def calc_ray_path(self, ray_origin, ray_direction, OBJ_list):
        hit_offset = 0.001
        ray_pos = [ray_origin]
        for kShoot in range(10):
            ray_start = ray_pos[-1] + hit_offset * ray_direction
            hit_pos = np.zeros((len(OBJ_list),2))
            hit_direction = np.zeros((len(OBJ_list),2))
            hit_count = np.zeros((len(OBJ_list),))
            origin_obj = np.matmul(OBJ_list.rot, ray_start - OBJ_list.origin)
            direction_obj = np.matmul(OBJ_list.rot, ray_direction)
            for kOBJ in range(len(OBJ_list)):
                hit_obj, tangent_obj = self.intersection(OBJ_list[kOBJ], origin_obj, direction_obj)
                if len(hit_obj)==2:
                    normal_obj = np.array([tangent_obj[1], -tangent_obj[0]])
                    sign_normal = -np.sign(np.dot(ray_direction, normal_obj))
                    hit = np.matmul(OBJ_list[kOBJ].rot.T, hit_obj.reshape((2,1))).T[0] + OBJ_list[kOBJ].origin
                    normal = np.matmul(OBJ_list[kOBJ].rot.T, sign_normal*normal_obj)
                    reflect = ray_direction - 2 * np.dot(ray_direction, normal) * normal
                    reflect = reflect / np.linalg.norm(reflect)
                    hit_pos[kOBJ] = hit
                    hit_direction[kOBJ] = reflect
                    hit_count[kOBJ] = 1
            if np.sum(hit_count) == 0:
                break
            else:
                idx = np.where(hit_count==1)[0]
                hit_distance = np.dot((hit_pos[idx] - ray_pos[-1]), ray_direction)
                hit_distance[hit_distance <=0] = 1e12
                ind = np.argmin(hit_distance)
                ray_pos.append(hit_pos[idx[ind]])
                ray_direction = hit_direction[idx[ind]]
        ray_pos.append(ray_pos[-1] + 10 * ray_direction)
        return np.array(ray_pos)