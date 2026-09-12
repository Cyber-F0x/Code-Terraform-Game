class ScanTarget():
    def echo(self) -> None:
    	    print(self.id,self.ammount,self.coords)

    def update_delivered(self):
        self.ammount = self.ammount - 1
    
    def __init__(self,id,ammount,coords):
    	    self.id = id
            self.ammount = ammount
            self.coords = coords

def find_fragment_coords(data,fragment) -> List:
        # pullout coords
        for each_fragment in data:
            if fragment in each_fragment.fragment_id:
                return(each_fragment.coords)
            

while True:
    self.discard()
    orders = get_component("bio_exchange_1").active_order()
    if orders != None:
        collection_targets = []
        scan_data = self.scan()
        
        # pullout coords
        '''
        # Potentially a better solution but will need tweaking.
        for each_fragment_location in scan_data:
            if orders.requires[0] in each_fragment_location.fragment_id:
                new_scan_target = ScanTarget(each_fragment_location.fragment_id
                                             ,orders.requires[each_fragment_location.fragment_id],
                                             each_fragment_location.coords)
                new_scan_target.echo()
                collection_targets.append(new_scan_target)
        '''     
        
        
        for each_requirment in orders.requires:
            coords = find_fragment_coords(scan_data,each_requirment)
            new_scan_target = ScanTarget(each_requirment,orders.requires[each_requirment],coords)
            collection_targets.append(new_scan_target)
        
        for each_target in collection_targets:
            # There is a bug here 
            # Todo fix
            collected = 0 
            while collected != each_target.ammount:
                if self.cargo == None:
                    self.collect(each_target.coords)
                    #each_target.update_delivered()
                    collected += 1
            
        orders = None
        #for each_requirement in orders.:
        #    find_fragment(data, each_requirement)#
        
                        
            
