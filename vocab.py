from aenea import (
    Text,
)

vocabWord = {
    "async": Text("async"),
    "await": Text("await"),

    "test expect": Text("expect().to.equal()"),
    "test subset": Text("expect().to.containSubset()"),

    "todo": Text("// TODO: "),
    "environment": Text("NODE_ENV"),

    "fulfilment order": Text("fulfilmentOrder"),
    "fulfilment": Text("fulfilment"),
    "sequelize find all": Text("const r = await models..findAll({where: {}}))"),
    "sequelize find one": Text("const r = await models..findOne({where: {}}))"),
    "sequelize find by id": Text("const r = await models..findById()"),
    #"": Text(""),
}
