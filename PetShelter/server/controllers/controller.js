const { req, res } = require('express');
const { Pet } = require('../models/models')
module.exports = {
    //CREATE
    createPet: (req,res) => {
        const { name, type, description, skill1, skill2, skill3 } = req.body;
        console.log(req.body)
        Pet.create(req.body)
            .then(pet => res.json({message: "success", results: pet}))
            .catch(err => res.json({message: "error", results:err}));
    },
    //READ
    getAllPets: (req,res) => {
        Pet.find()
        .then(pet => res.json({message: "success", results: pet}))
        .catch(err => res.json({message: "error", results: err}));
    },
    getPet: (req,res) => {
        Pet.findById(req.params._id)
        .then(pet => res.json({message: "success", results: pet}))
        .catch(err => res.json({message: "error", results: err}));
    },
    //UPDATE
    updatePet: (req,res) => {
        Pet.findByIdAndUpdate(req.params._id, req.body, {new:true, runValidators: true})
        .then(pet => res.json({message: "success", results: pet}))
        .catch(err => res.json({message: "error", results: err}));
    },
    addSkill: (req,res) => {
        Pet.findByIdAndUpdate(req.params._id, { $push: {skills: req.body }}, { new: true, runValidators: true })
        .then(pet => res.json({message: "success", results: pet}))
        .catch(err => res.json({message: "error", results: err}));
    },
    //DELETE
    deletePet: (req,res) => {
        Pet.findByIdAndDelete(req.params._id)
        .then(pet => res.json({message: "success", results: pet}))
        .catch(err => res.json({message: "error", results: err}));
    }
}