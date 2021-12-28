import bpy
from random import *

print("")
print("")
print("")

n = 5
spaces = []
spacesNext = []

for x in range(n):
    spaces.append([])
    spacesNext.append([])
    for y in range(n):
        spaces[x].append([])
        spacesNext[x].append([])
        for z in range(n):
            spaces[x][y].append("empty")
            spacesNext[x][y].append("empty")


cubeList = []
for x in range(n):
    for y in range(n):
        for z in range(n):
            if uniform(0,1) < 0.5:
                mat = bpy.data.materials.get("Material.001")
                bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z))
                obj = bpy.context.object
                obj.location = (x,y,z)
                obj.keyframe_insert(data_path="location", frame=0, index=-1)
                cubeList.append(obj)
                spaces[x][y][z] = "full"
                bpy.ops.object.shade_smooth()

                colors = [[1,0.847,0.0,1], [0,1,0,1], [0,0.624,0.624,1], [0, 0, 1, 1], [1,0,1,1], [1,0,0,1], [1,0.3,0,1]]

                choice = randint(0, len(colors)-1)
                mat1 = bpy.data.materials.get("Material.001")
                nodes = mat1.node_tree.nodes
                bsdf = nodes.get("Émission")
                bsdf.inputs["Color"].default_value = (colors[choice][0], colors[choice][1], colors[choice][2], colors[choice][3])
                bsdf.inputs["Color"].keyframe_insert(data_path="default_value", frame=0, index=-1)
                shade = nodes.get("Shader de mélange")
                shade.inputs["Fac"].default_value = 0.607
                shade.inputs["Fac"].keyframe_insert(data_path="default_value", frame=0, index=-1)
                obj.data.materials.append(mat)


def isEmpty(x,y,z):
    if x < 0 or x > n-1:
        return False

    if y < 0 or y > n-1:
        return False

    if z < 0 or z > n-1:
        return False


    if spaces[int(x)][int(y)][int(z)] == "full":
        return False

    if spacesNext[int(x)][int(y)][int(z)] == "full":
        return False

    return True

list_isempty = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
shuffle(list_isempty)
print(list_isempty)

for curFrame in range(0,500,10):
    for cube in cubeList:
        curX,curY,curZ = cube.location

        for i in range (0,5):
            if isEmpty(int(curX+list_isempty[i][0]), int(curY + list_isempty[i][1]), int(curZ + list_isempty[i][2])):
                cube.location = (curX+list_isempty[i][0], curY+list_isempty[i][1], curZ+list_isempty[i][2])
                break

        curX,curY,curZ = cube.location
        spacesNext[int(curX)][int(curY)][int(curZ)] = "full"
        cube.keyframe_insert(data_path="location", frame=curFrame, index=-1)

        colors = [[1,0.847,0.0,1], [0,1,0,1], [0,0.624,0.624,1], [0, 0, 1, 1], [1,0,1,1], [1,0,0,1], [1,0.3,0,1]]

        choice = randint(0, len(colors)-1)

        bsdf = nodes.get("Émission")
        bsdf.inputs["Color"].default_value = (colors[choice][0], colors[choice][1], colors[choice][2], colors[choice][3])
        bsdf.inputs["Color"].keyframe_insert(data_path="default_value", frame=curFrame, index=-1)
        shade = nodes.get("Shader de mélange")
        shade.inputs["Fac"].default_value = 0.840
        shade.inputs["Fac"].keyframe_insert(data_path="default_value", frame=randint(1,500), index=-1)


    for x in range(n):
        for y in range(n):
            for z in range(n):
                spaces[x][y][z] = spacesNext[x][y][z]
                spacesNext[x][y][z] = "empty"
                shuffle(list_isempty)

print(spaces)