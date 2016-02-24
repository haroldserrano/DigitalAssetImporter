#Digital Asset Importer for Blender 3D
#Author: Harold Serrano
#Website: www.haroldserrano.com
#Date: 2/23/16


import bpy


#class for Model. This contains all the attributes of the model
class Model:
    def __init__(self):
        self.vertices=[]
        self.normals=[]
        self.uv=[]
        self.index=[]


def main():
    
    #1. create a Model object
    model=Model()
    
    #2. Search for all objects in the  scene
    for models in bpy.context.scene.objects:
        
        #3. check if the object is a 3D mesh
        if(models.type=="MESH"):
            
            #4. get the name of the MESH
            name=models.name
            print("Name of Mesh: %s"%name)
            
            
            #5. loop through each vertex and print it out each vertex
            for i,indices in enumerate(bpy.context.scene.objects[name].data.loops):
                
                #6. read the vertices
                vertices=bpy.context.scene.objects[name].data.vertices[indices.vertex_index].co
                
                #7. append the vertices to the class member of the Model class
                model.vertices.append(vertices)
                
                #8. read the normals
                normals=bpy.context.scene.objects[name].data.vertices[indices.vertex_index].normal
                
                #9. append the normals to the class member of the Model class
                model.normals.append(normals)
                
                
                #10. Get the indexes that may be used in the GPU
                model.index.append(i)
            
            #11. Check if the uv_layers have been enabled in the model properties
            if(bpy.context.scene.objects[name].data.uv_layers):
                
                #12. Loop through the UV coordinates
                for uvCoordinates in bpy.context.scene.objects[name].data.uv_layers.active.data:
                    
                    #13. get uv coordinates of model
                    
                    model.uv.append(uvCoordinates.uv)
            
            
            #14. Print all vertices
            print("<vertices>",end="")
            
            for i in range(0,len(model.vertices)):
                
                print("%f %f %f "%tuple(model.vertices[i]),end="")
            
            print("</vertices>")
            
            print()
            print()
            
            #15. Print all normals
            print("<normals>",end="")
            
            for i in range(0,len(model.normals)):
                
                print("%f %f %f "%tuple(model.normals[i]),end="")
            
            print("</normals>")
            
            print()
            print()
            
            #16. Print all uv coordinates
            print("<uv>",end="")
            
            for i in range(0,len(model.uv)):
                
                print("%f %f "%tuple(model.uv[i]),end="")
                
            print("</uv>")

            print()
            print()
        
            print("<index>",end="")
            
            #17. Print out the indices
            for i in model.index:
                print("%d "%i,end="")
    
            print("</index>")
            
            print()


if __name__ == '__main__':
    main()