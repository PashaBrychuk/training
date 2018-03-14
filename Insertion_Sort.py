classes = get_all_subclasses(BaseGame)
    for cls in classes:}
       .....

def get_all_subclasses(cls):
    return cls.__subclasses() + [g for s in cls.__subclasses()
                                   for g in get_all_subclasses(s)]