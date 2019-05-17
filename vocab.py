from aenea import (
    Text,
)

vocabWord = {
    "async": Text("async"),
    "await": Text("await"),

    "test expect": Text("expect().to.equal()"),
    "test subset": Text("expect().to.containSubset()"),
    "test describe": Text("describe('', async () => { });"),
    "test it": Text("it('', async () => { });"),
    "test length": Text("expect().lengthOf()"),

    # "": Text(""),

    "partner": Text("fulfilmentPartner"),
    "base test records": Text("baseTestRecords"),
    "partner token": Text("fulfilmentPartnerToken"),
    "partner user": Text("fulfilmentPartnerUser"),
    "supplier user": Text("supplierUser"),
    "supplier token": Text("supplierToken"),

    "todo": Text("// TODO: "),
    "environment": Text("NODE_ENV"),

    "fulfilment order": Text("fulfilmentOrder"),
    "fulfilment": Text("fulfilment"),
    "sequelize find all": Text("const r = await models..findAll({where: {}}))"),
    "sequelize find one": Text("const r = await models..findOne({where: {}}))"),
    "sequelize find by id": Text("const r = await models..findById()"),

    #"": Text(""),

    "constant": Text("coe"),
    "arrow function": Text("afb"),

    "swagger": Text("swagger"),
}
