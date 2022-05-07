const PetController = require('../controllers/controller');

module.exports = app => {
    //CREATE
    app.post('/api/pets', PetController.createPet);
    //READ
    app.get('/api/pets', PetController.getAllPets);
    app.get('/api/pets/:_id', PetController.getPet);
    //UPDATE
    app.put('/api/pets/:_id', PetController.updatePet);
    //DELETE
    app.delete('/api/pets/:_id', PetController.deletePet);
}