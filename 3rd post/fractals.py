import bpy
from random import *
from os import system

cls = lambda: system('cls')
cls() #this function call will clear the console

def cubes(x,y,z,size,number,globalI, variable = 0):
    global colors, materials
    liste = [[size - size/4,0,0], [0,size - size/4,0], [0,0,size - size/4], [-size + size/4,0,0], [0,-size+size/4,0], [0,0,-size+size/4]]
    for i in range(6):
        if randint(0,2) == 0 or randint(0,2) == 1:
            if i != globalI:
                if randint(0,1):
                    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=0.5, location=(x + liste[i][0],y + liste[i][1],z + liste[i][2]))
                else:
                    bpy.ops.mesh.primitive_cube_add(size=1, location=(x + liste[i][0],y + liste[i][1],z + liste[i][2]))
                bpy.ops.object.shade_smooth()
                obj = bpy.context.object
                obj.scale[0] = 0
                obj.scale[1] = 0
                obj.scale[2] = 0
                obj.keyframe_insert(data_path="scale", frame= 15 + variable, index=-1)
                obj.scale[0] = size/2
                obj.scale[1] = size/2
                obj.scale[2] = size/2
                obj.keyframe_insert(data_path="scale", frame= 20 + variable, index=-1)
                choice_material = randint(0, len(materials)-1)
                mat = bpy.data.materials.get(materials[choice_material])
                obj.data.materials.append(mat)
                if number != 0:
                    print(i, globalI)
                    if i < 3:
                        cubes(x + liste[i][0],y + liste[i][1],z + liste[i][2], obj.scale[0],number-1,i+3, variable + 15)
                    else:
                        cubes(x + liste[i][0],y + liste[i][1],z + liste[i][2], obj.scale[0],number-1,i-3, variable + 15)


bpy.ops.mesh.primitive_cube_add(size=0, location=(0,0,0))
obj = bpy.context.object
obj.scale[0] = 0
obj.scale[1] = 0
obj.scale[2] = 0
obj.keyframe_insert(data_path="scale", frame= 0, index=-1)
obj.scale[0] = 2
obj.scale[1] = 2
obj.scale[2] = 2
obj.keyframe_insert(data_path="scale", frame= 10, index=-1)
colors = [[0,1,0,1], [0, 0, 1, 1], [1,0,0,1]]
materials = ["Material.004", "Material.005", "Material.006"]
choice_material = randint(1, len(materials)-1)
mat = bpy.data.materials.get(materials[choice_material])
obj.data.materials.append(mat)


cubes(0,0,0,2,5,6)