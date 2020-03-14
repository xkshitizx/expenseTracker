import datetime
i=0

content={
    '{i}':{
            "Category":'{cat}',
            "Money":'{money}',
            "Date":'{d}'
        }
}

cat=input("Choose a category:\n 1. Food \n 2. Clothing \n 3. Education\n 4. Travel")
d=datetime.datetime.today()
money=input("how much did you spend??")

content.update({
    i:{
            "Category":cat,
            "Money":money,
            "Date":d
        }
})
print(content)
