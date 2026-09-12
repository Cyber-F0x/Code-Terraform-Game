shop = get_component("shop")
collector = get_component("bio_collector_1")

def ready_status(specimin)-> bool:
    for each_reagent in self.loaded_reagents:
            loaded_quantity = self.loaded_reagents[each_reagent]
            if specimin.recipe[each_reagent] != loaded_quantity:
                return False
    return True


while True:
    specimin = self.specimen
    
    if specimin is None:
        transfer = self.take_from(collector)
        if transfer.status == "busy":
            sleep(0.2)
            continue
        if transfer.status != "ok":
            print(transfer.status)
            sleep(0.2)
            continue
        continue
        
    if specimin.stage == "collected":
        analysis = self.analyze()
        if analysis.status == "busy":
            sleep(0.2)
            continue
        if analysis.status != "ok":
            print(analysis.message)
            sleep(0.2)
            continue
        
        continue

    
    #buy reagents and load 
    self.unload_reagents()
    
    # Update me
    self.input.flush()
    
    self.input.connect("inventory")
    for each_reagent in specimin.recipe:
        reagent_name = each_reagent
        quantity = specimin.recipe[each_reagent]
        purchase = shop.buy(reagent_name, quantity)
        if purchase.status != "ok":
            print(purchase.message)
            break
        self.input.take(reagent_name,quantity)
        self.load(reagent_name,quantity)

    if not ready_status(specimin):
        print("Error, something went wrong with loaded reagents, quantity values dont match")
        break
    extraction = self.extract()
    if extraction.status == "ok":
        self.output.connect("inventory")
        self.output.send(specimin.fragment_id,1)
        continue    
    if extraction.status == "busy":
        sleep(0.2)
        continue
    
    