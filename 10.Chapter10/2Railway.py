class Railway:
    form = "RailForm"

    def PrintData(self):
        print(
            "Name is",
            self.name,
        )
        print(
            "The train name is",
            self.train,
        )

MyAppl = Railway()
MyAppl.name = "Aditya"
MyAppl.train = "Tejas Express"
MyAppl.PrintData()
