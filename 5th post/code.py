import bpy
from mathutils import Vector
import math
from random import randint, shuffle

print("\n \n \n")

###################################
########## setup scene ############
###################################

_cursor = bpy.context.scene.cursor

_cursor.location = Vector((0,0,0))
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
cubes = []
materials = ["Material.001", "Material.002"]
# Material.001 = Bleu
# Material.002 = Rouge
red_positions = [Vector((15.5, 15.5, -45.0)), Vector((16.5, 15.5, -45.0)), Vector((17.5, 15.5, -45.0)), Vector((18.5, 16.5, -45.0)), Vector((15.5, 21.5, -45.0)), Vector((16.5, 21.5, -45.0)), Vector((17.5, 21.5, -45.0)), Vector((18.5, 20.5, -45.0)), Vector((14.5, 16.5, -45.0)), Vector((14.5, 17.5, -45.0)), Vector((14.5, 18.5, -45.0)), Vector((14.5, 19.5, -45.0)), Vector((14.5, 20.5, -45.0)), Vector((13.5, 22.5, -45.0)), Vector((13.5, 14.5, -45.0)), Vector((12.5, 22.5, -45.0)), Vector((12.5, 14.5, -45.0)), Vector((12.5, 21.5, -45.0)), Vector((12.5, 15.5, -45.0)), Vector((12.5, 20.5, -45.0)), Vector((12.5, 16.5, -45.0)), Vector((12.5, 19.5, -45.0)), Vector((12.5, 17.5, -45.0)), Vector((12.5, 18.5, -45.0))]
blue_positions = [Vector((20.5, 15.5, -45.0)), Vector((20.5, 15.5, -45.0)), Vector((21.5, 15.5, -45.0)), Vector((20.5, 16.5, -45.0)), Vector((22.5, 15.5, -45.0)), Vector((20.5, 17.5, -45.0)), Vector((23.5, 15.5, -45.0)), Vector((20.5, 18.5, -45.0)), Vector((20.5, 19.5, -45.0)), Vector((20.5, 20.5, -45.0)), Vector((20.5, 21.5, -45.0)), Vector((24.5, 14.5, -45.0)), Vector((24.5, 22.5, -45.0)), Vector((25.5, 14.5, -45.0)), Vector((25.5, 22.5, -45.0)), Vector((25.5, 15.5, -45.0)), Vector((25.5, 21.5, -45.0)), Vector((25.5, 16.5, -45.0)), Vector((25.5, 20.5, -45.0)), Vector((25.5, 17.5, -45.0)), Vector((25.5, 19.5, -45.0)), Vector((25.5, 18.5, -45.0))]


for i in range(len(red_positions)):
    (x,y,z) = red_positions[0].to_tuple()
    del red_positions[0]
    red_positions.append(Vector((x+1.5,y-1,z)))

for j in range(len(blue_positions)):
    (x,y,z) = blue_positions[0].to_tuple()
    del blue_positions[0]
    blue_positions.append(Vector((x+1.5,y-1,z)))
    
shuffle(red_positions)
shuffle(blue_positions)
#############################################
########## main cube & movements ############
#############################################

bpy.ops.mesh.primitive_cube_add(size=1)
obj = bpy.context.object
cubes.append(obj)
obj.location = (0.5, 0.5, 0.5)
bpy.context.scene.cursor.location = Vector((1,1,0))
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
choice_material = randint(0, len(materials)-1)
mat = bpy.data.materials.get(materials[choice_material])
obj.data.materials.append(mat)
rotation = bpy.context.active_object.rotation_euler

for i in range(2):
    if i == 0:
        images = 0
    else:
        images += 60
    obj.keyframe_insert(data_path="rotation_euler", frame=images, index=-1)
    rotation[0] = math.radians(-90)
    obj.keyframe_insert(data_path="rotation_euler", frame=images + 10, index=-1)


    obj.keyframe_insert(data_path="location", frame=images + 10, index=-1)
    obj.location[1] += 1
    rotation[0] = math.radians(0)
    obj.keyframe_insert(data_path="rotation_euler", frame=images + 11, index=-1)
    obj.keyframe_insert(data_path="location", frame=images + 11, index=-1)


    obj.keyframe_insert(data_path="rotation_euler", frame=images + 15, index=-1)
    rotation[1] = math.radians(90)
    obj.keyframe_insert(data_path="rotation_euler", frame=images + 25, index=-1)


    obj.keyframe_insert(data_path="location", frame=images + 25, index=-1)
    obj.location[0] += 1
    obj.location[1] -= 1
    rotation[1] = math.radians(0)
    rotation[2] = math.radians(-90)
    obj.keyframe_insert(data_path="location", frame=images + 26, index=-1)
    obj.keyframe_insert(data_path="rotation_euler", frame=images + 26, index=-1)


    obj.keyframe_insert(data_path="rotation_euler", frame=images + 30, index=-1)
    rotation[1] = math.radians(90)
    obj.keyframe_insert(data_path="rotation_euler", frame=images + 40, index=-1)


    obj.keyframe_insert(data_path="location", frame=images + 40, index=-1)
    rotation[2] = math.radians(0)
    obj.location[0] -= 1
    obj.keyframe_insert(data_path="rotation_euler", frame=images + 41, index=-1)
    obj.keyframe_insert(data_path="location", frame=images + 41, index=-1)


    obj.keyframe_insert(data_path="rotation_euler", frame=images + 45, index=-1)
    rotation[1] = 0
    obj.keyframe_insert(data_path="rotation_euler", frame=images + 55, index=-1)

##############################################################
########### clone creation & movements of all ################
##############################################################

variable = 1
y = 0.5
x = 2.5

for j in range(10):
    for i in range(2):
        for z in range(1, 20):
            bpy.ops.mesh.primitive_cube_add(size=1, location = (x + variable-1, y, 0.5))
            bpy.context.scene.cursor.location = Vector((x + 0.5 + variable - 1, y + 0.5,0))
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            obj1 = bpy.context.object
            cubes.append(obj1)
            constraint0 = obj1.constraints.new('CHILD_OF')
            constraint0.influence = 1
            bpy.context.object.constraints['Child Of'].keyframe_insert(data_path="influence", frame=0, index=-1)
            constraint0.target = obj
            constraint0.use_location_x = False
            constraint0.use_location_y = False
            constraint0.use_location_z = False
            choice_material = randint(0, len(materials)-1)
            mat = bpy.data.materials.get(materials[choice_material])
            obj1.data.materials.append(mat)

            for k in range(2):
                if k == 0:
                    images = 0
                else:
                    images += 60
                obj1.keyframe_insert(data_path="location", frame=images + 10, index=-1)
                obj1.location[1] += 1
                obj1.keyframe_insert(data_path="location", frame=images + 11, index=-1)


                obj1.keyframe_insert(data_path="location", frame=images + 25, index=-1)
                obj1.location[0] += 1
                obj1.location[1] -= 1
                obj1.keyframe_insert(data_path="location", frame=images + 26, index=-1)


                obj1.keyframe_insert(data_path="location", frame=images + 40, index=-1)
                obj1.location[0] -= 1
                obj1.keyframe_insert(data_path="location", frame=images + 41, index=-1)
            
            variable += 2
        variable = 1
        if i % 2 == 0:
            x -= 1
        else:
            x = 2.5
        y += 2

##########################################
######### "boom" preparation #############
##########################################

length = len(cubes)
var1 = len(cubes)//2
var2 = (len(cubes)//2) + 1

middle = cubes[var1 - 9]
fst_circle = []
scd_circle = []
thrd_circle = []
frth_circle = []

for i in range(length):
    (cubeX, cubeY, cubeZ) = cubes[i].location[:]
    distance = int(math.sqrt((cubeX - middle.location[0])**2 + (cubeY - middle.location[1])**2))
    if distance <= 6:
        fst_circle.append(cubes[i])
    elif distance <= 10:
        scd_circle.append(cubes[i])
    elif distance <= 15:
        thrd_circle.append(cubes[i])
    else:
        frth_circle.append(cubes[i])        

#########################################
########## center destruction ###########
#########################################
begin = 130
for i in range(len(fst_circle)):
    time = randint(15, 30)
    obj = fst_circle[i]
    obj.keyframe_insert(data_path="location", frame=begin, index=-1)
    if len(blue_positions) > 0 or len(red_positions) > 0:
        if obj.material_slots[0].name == "Material.001" and len(blue_positions) > 0:
            obj.location = blue_positions[0]
            del blue_positions[0]
        elif obj.material_slots[0].name == "Material.002" and len(red_positions) > 0:
            obj.location = red_positions[0]
            del red_positions[0]
    
        for m in obj.constraints:
            if m.type == "CHILD_OF":
                m.influence = 1
                obj.constraints['Child Of'].keyframe_insert(data_path="influence", frame=125, index=-1)
                m.influence = 0
                obj.constraints['Child Of'].keyframe_insert(data_path="influence", frame=126, index=-1)
            
        obj.keyframe_insert(data_path="rotation_euler", frame=begin, index=-1)
        (obj.rotation_euler[0], obj.rotation_euler[1], obj.rotation_euler[2])  = (math.radians(360), math.radians(360), math.radians(360))
        obj.keyframe_insert(data_path="rotation_euler", frame=230, index=-1)
    else:
        obj.keyframe_insert(data_path="rotation_euler", frame=begin, index=-1)
        (obj.rotation_euler[0], obj.rotation_euler[1], obj.rotation_euler[2])  = (math.radians(randint(0, 720)), math.radians(randint(0, 720)), math.radians(randint(0, 720)))
        obj.keyframe_insert(data_path="rotation_euler", frame=begin + time, index=-1)
        obj.hide_viewport = False
        obj.keyframe_insert(data_path="hide_viewport", frame=0, index=-1)
        obj.hide_viewport = True
        obj.keyframe_insert(data_path="hide_viewport", frame=begin + time, index=-1)
        obj.hide_render = False
        obj.keyframe_insert(data_path="hide_render", frame=0, index=-1)
        obj.hide_render = True
        obj.keyframe_insert(data_path="hide_render", frame=begin + time, index=-1)
    obj.keyframe_insert(data_path="location", frame=230, index=-1)

#########################################
######### second part destruction #######
#########################################
for i in range(len(scd_circle)):
    interval = 230
    variable = 133
    obj = scd_circle[i]
    obj.keyframe_insert(data_path="location", frame=variable, index=-1)
    
    if len(blue_positions) > 0 or len(red_positions) > 0:
        if obj.material_slots[0].name == "Material.001" and len(blue_positions) > 0:
            obj.location = blue_positions[0]
            del blue_positions[0]
        elif obj.material_slots[0].name == "Material.002" and len(red_positions) > 0:
            obj.location = red_positions[0]
            del red_positions[0]
    
        for m in obj.constraints:
            if m.type == "CHILD_OF":
                m.influence = 1
                obj.constraints['Child Of'].keyframe_insert(data_path="influence", frame=125, index=-1)
                m.influence = 0
                obj.constraints['Child Of'].keyframe_insert(data_path="influence", frame=126, index=-1)
        
        obj.keyframe_insert(data_path="rotation_euler", frame=variable, index=-1)
        (obj.rotation_euler[0], obj.rotation_euler[1], obj.rotation_euler[2])  = (math.radians(360), math.radians(360), math.radians(360))
        obj.keyframe_insert(data_path="rotation_euler", frame=interval, index=-1)
    else:
        obj.location[2] -= 30
        obj.keyframe_insert(data_path="rotation_euler", frame=variable, index=-1)
        (obj.rotation_euler[0], obj.rotation_euler[1], obj.rotation_euler[2])  = (math.radians(randint(0, 720)), math.radians(randint(0, 720)), math.radians(randint(0, 720)))
        obj.keyframe_insert(data_path="rotation_euler", frame=interval, index=-1)
        obj.hide_viewport = False
        obj.keyframe_insert(data_path="hide_viewport", frame=0, index=-1)
        obj.hide_viewport = True
        obj.keyframe_insert(data_path="hide_viewport", frame=interval, index=-1)
        obj.hide_render = False
        obj.keyframe_insert(data_path="hide_render", frame=0, index=-1)
        obj.hide_render = True
        obj.keyframe_insert(data_path="hide_render", frame=interval, index=-1)
    obj.keyframe_insert(data_path="location", frame=interval, index=-1)

#########################################
######### third part destruction ########
#########################################
for i in range(len(thrd_circle)):
    time = 210
    variable = 136
    obj = thrd_circle[i]
    obj.keyframe_insert(data_path="location", frame=variable, index=-1)
    obj.location[2] -= 30
    obj.keyframe_insert(data_path="rotation_euler", frame=variable, index=-1)
    (obj.rotation_euler[0], obj.rotation_euler[1], obj.rotation_euler[2])  = (math.radians(randint(0, 720)), math.radians(randint(0, 720)), math.radians(randint(0, 720)))
    obj.keyframe_insert(data_path="rotation_euler", frame=time, index=-1)
    obj.hide_viewport = False
    obj.keyframe_insert(data_path="hide_viewport", frame=0, index=-1)
    obj.hide_viewport = True
    obj.keyframe_insert(data_path="hide_viewport", frame=time, index=-1)
    obj.hide_render = False
    obj.keyframe_insert(data_path="hide_render", frame=0, index=-1)
    obj.hide_render = True
    obj.keyframe_insert(data_path="hide_render", frame=time, index=-1)
    obj.keyframe_insert(data_path="location", frame=time, index=-1)

#########################################
####### fix a bug on the last cube ######
#########################################

for m in frth_circle[len(frth_circle)-1].constraints:
    print(m.type)
    if m.type == "CHILD_OF":
        CO_constraint = m
        context_py = bpy.context.copy()
        context_py["constraint"] = CO_constraint
        bpy.ops.constraint.childof_set_inverse(context_py, constraint=CO_constraint.name, owner='OBJECT')

#########################################
######### fourth part destruction #######
#########################################
for i in range(len(frth_circle)):
    obj = frth_circle[i]
    variable = 210
    interval = 139
    obj.keyframe_insert(data_path="location", frame=interval, index=-1)
    obj.location[2] -= 30
    obj.hide_viewport = False
    obj.keyframe_insert(data_path="hide_viewport", frame=0, index=-1)
    obj.hide_viewport = True
    obj.keyframe_insert(data_path="hide_viewport", frame=variable, index=-1)
    obj.hide_render = False
    obj.keyframe_insert(data_path="hide_render", frame=0, index=-1)
    obj.hide_render = True
    obj.keyframe_insert(data_path="rotation_euler", frame=interval, index=-1)
    (obj.rotation_euler[0], obj.rotation_euler[1], obj.rotation_euler[2])  = (math.radians(randint(0, 720)), math.radians(randint(0, 720)), math.radians(randint(0, 720)))
    obj.keyframe_insert(data_path="rotation_euler", frame=variable, index=-1)
    obj.keyframe_insert(data_path="hide_render", frame=variable, index=-1)
    obj.keyframe_insert(data_path="location", frame=variable, index=-1)