import bpy
import math
import random


materials = []
for i in range(2)
    materials.append(Material.00 + str(i+1))

positions = []
positions_lamps = []

def isPrime(n)
    if n  2
        return False
    for number in range(2, int(math.sqrt(n)+1))
        if n % number == 0
            return False

    return True

n = 0
x = 0
y = 0
label = 1
if isPrime(label)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0))
    obj = bpy.context.object
    mat = bpy.data.materials.get(materials[random.randint(0,len(materials))-1])
    obj.data.materials.append(mat)
    bpy.ops.object.light_add(radius=0.5, location=(x+1, y+i, 0))
    obj1 = bpy.context.object
    positions.append(obj)
    positions_lamps.append(obj1)
label += 1

for o in range(15)
    for i in range(2 + n)
        if isPrime(label)
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x+1, y+i, 0))
            obj = bpy.context.object
            mat = bpy.data.materials.get(materials[random.randint(0,len(materials))-1])
            obj.data.materials.append(mat)
            bpy.ops.object.light_add(radius=0.5, location=(x+1, y+i, 0))
            obj1 = bpy.context.object
            positions.append(obj)
            positions_lamps.append(obj1)
        label += 1

    y += 1 + n

    for j in range(2 + n)
        if isPrime(label)
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x-j, y, 0))
            obj = bpy.context.object
            mat = bpy.data.materials.get(materials[random.randint(0,len(materials))-1])
            obj.data.materials.append(mat)
            bpy.ops.object.light_add(radius=0.5, location=(x-j, y, 0))
            obj1 = bpy.context.object
            positions.append(obj)
            positions_lamps.append(obj1)
        label += 1

    x -= 1 + n
    y -= 1

    for k in range(2 + n)
        if isPrime(label)
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y-k, 0))
            obj = bpy.context.object
            mat = bpy.data.materials.get(materials[random.randint(0,len(materials))-1])
            obj.data.materials.append(mat)
            bpy.ops.object.light_add(radius=0.5, location=(x, y-k, 0))
            obj1 = bpy.context.object
            positions.append(obj)
            positions_lamps.append(obj1)
        label += 1

    y -= 1 + n
    x += 1

    for l in range(2 + n)
        if isPrime(label)
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x + l, y, 0))
            obj = bpy.context.object
            mat = bpy.data.materials.get(materials[random.randint(0,len(materials))-1])
            obj.data.materials.append(mat)
            bpy.ops.object.light_add(radius=0.5, location=(x + l, y, 0))
            obj1 = bpy.context.object
            positions.append(obj)
            positions_lamps.append(obj1)
        label += 1

    x += 1 + n
    n += 2

print(positions, len(positions))

def check(x,y,z)
#    global positions
    neighbours = 0
    for k in range(len(positions))
        if (x + 1.0, y, z)== (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1
        if (x - 1.0, y, z) == (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1
        if (x, y + 1.0, z) == (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1
        if (x, y-1.0, z) == (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1
        if (x+1.0, y+1.0, z) == (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1
        if (x+1.0, y-1.0, z) == (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1
        if (x-1.0, y+1.0, z) == (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1
        if (x-1.0, y-1.0, z) == (positions[k].location[0], positions[k].location[1], positions[k].location[2])
            neighbours += 1

    return neighbours

counter = 0
difference = 0
main = random.randint(10,15)
frame_randomised =  random.randint(10, 25)
something = random.randint(15,25)

for objects in positions
    objects.scale[2] = check(objects.location[0], objects.location[1], objects.location[2])
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame=main, index=-1)
    if objects.scale[2]  0
        difference = 0.5
    else
        difference = 0
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= main + main + frame_randomised, index=-1)
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame=main + main + frame_randomised + something, index=-1)

    objects.scale[2] = check(objects.location[0], objects.location[1], objects.location[2])
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame=main + main + frame_randomised + something + frame_randomised, index=-1)
    if objects.scale[2]  0
        difference = 0.5
    else
        difference = 0
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= main + main + frame_randomised + something + frame_randomised + something, index=-1)
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame=main + main + frame_randomised + something + frame_randomised + something + something, index=-1)

    frames = random.randint(15, 25)
    objects.scale[2] = check(objects.location[0], objects.location[1], objects.location[2])
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= frames + main + main + frame_randomised + something + frame_randomised, index=-1)
    if objects.scale[2]  0
        difference = 0.5
    else
        difference = 0
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= frames + main + main + frame_randomised + something + frame_randomised + something, index=-1)
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= frames + main + main + frame_randomised + something + frame_randomised + something + something, index=-1)

    objects.scale[2] = check(objects.location[0], objects.location[1], objects.location[2])
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= frames + main + main + frame_randomised + something + frame_randomised + something + something + something, index=-1)
    if objects.scale[2]  0
        difference = 0.5
    else
        difference = 0
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= frames + main + main + frame_randomised + something + frame_randomised + something + something + something + something, index=-1)
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something, index=-1)


    objects.scale[2] = check(objects.location[0], objects.location[1], objects.location[2])
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something, index=-1)
    if objects.scale[2]  0
        difference = 0.5
    else
        difference = 0
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something, index=-1)
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something + something, index=-1)

    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something + something + frames, index=-1)
    if objects.scale[2]  0
        difference = 0.5
    else
        difference = 0
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something + something + frames + frames, index=-1)
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something + something + frames + frames + frames, index=-1)


    objects.scale[2] = check(objects.location[0], objects.location[1], objects.location[2])
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something + something + frames + frames + frames + frames, index=-1)
    if objects.scale[2]  0
        difference = 0.5
    else
        difference = 0
    positions_lamps[counter].location[2] = objects.scale[2]2 - difference
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something + something + frames + frames + frames + frames + frame_randomised, index=-1)
    positions_lamps[counter].location[2] = 0
    positions_lamps[counter].keyframe_insert(data_path=location, frame= something + frames + something + something + main + main + frame_randomised + something + frame_randomised + something + something + something + something + frames + frames + frames + frames + frame_randomised + frame_randomised, index=-1)

    main += random.randint(0,5)
    counter += 1