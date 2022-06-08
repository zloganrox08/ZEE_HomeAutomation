#imports
import xml.etree.ElementTree as ET
import json
from types import SimpleNamespace

#Variables
debug = 1

#functions
class SE_Blueprint() :
    main_model = None

    def __init__(self): 
        json_filepath = "test_SE_Export1.json"

        with open(json_filepath, 'r') as model_json :
            model_json = json.load(model_json)

        self.main_model = model_json
        
        self.Prefabs = self.main_model["Definitions"]["Prefabs"]
        #self.print_all_values(Prefabs)
        CubeGrids = []
        for prefab_key, prefab_value in self.Prefabs.items() :
            CubeGrids.append([prefab_key, prefab_value["CubeGrids"]])
        self.CubeGrids = CubeGrids
        
    def export_bluprint(self) : 
        for grid_key, grid_value in self.CubeGrids:
            # This is the loop for each individual grid
            # In terms of a model export, this should denote each individual part
            # Not physically connected

            # grid_key is relatively useless
            # grid_value is everything inside the CubeGrids
            # I think this is at the wrong level, may be bug #TODO

            model_out = None
            blocklist = grid_value["CubeGrid"]["CubeBlocks"]["MyObjectBuilder_CubeBlock"]
            
            print(blocklist)
            print(str(type(blocklist)))
            print("len(blocklist): " + str(len(blocklist)))

            for block in blocklist :
                # This loops through each block on the grid
                # Let's print its name
                if debug: print("Found block of type: " + str(block["SubtypeName"]))
                #if debug: print("block_info: " + str(block))


    def print_all_values(self, nested_dict) : 
        for key, value in nested_dict.items():
            if type(value) is dict:
                self.print_all_values(value)
            else:
                print(key, ":", value,"\n")


        blockcounts = {}
        for grid_key, grid_value in self.CubeGrids:
            # This is the loop for each individual grid
            # grid_key is relatively useless
            # grid_value is everything inside the CubeGrids
            # I think this is at the wrong level, may be bug #TODO
            blocklist = grid_value["CubeGrid"]["CubeBlocks"]["MyObjectBuilder_CubeBlock"]
            for block in blocklist :
                # This loops through each block on the grid
                # Let's print its name
                if debug: print("Found block of type: " + str(block["SubtypeName"]))
                #if debug: print("block_info: " + str(block))
                currblockname = block["SubtypeName"]
                print("currblockname:" + str(currblockname) + "," + str(type(currblockname)))
                #print("Here's the blockcounts: ")
                #print(blockcounts)
                try :
                    print(blockcounts[currblockname])
                    blockcounts[currblockname] += 1
                except KeyError :
                    blockcounts[str(currblockname)] = 1
        
        print("Here's the blockcounts: ")
        print(blockcounts)

if __name__ == "__main__" :
    print("If in debug, I'm going to count some blocks")
    debug_blueprint = SE_Blueprint()
    debug_blueprint.export_bluprint()
    debug_blueprint.calculate_block_counts()

#debug_blueprint = SE_Blueprint()
#debug_blueprint.export_bluprint()
#debug_blueprint.print_all_values(debug_blueprint)
#debug_blueprint.calculate_block_counts()