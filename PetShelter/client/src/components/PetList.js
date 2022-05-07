import React, { useEffect, useState } from 'react'
import { Link } from '@reach/router';
import axios from 'axios';
import DeleteButton from './DeleteButton';

const PetList = () => {
    const [pets, setPet] = useState([]);
    useEffect(() => {
        axios.get('http://localhost:8000/api/pets')
            .then(res => setPet(res.data.results));
    }, [])
    const removeFromDom = petId => {
        setPet(pets.filter(pet => pet._id !== petId));
    }
    return (
        <div>
            {pets.map((pet, idx) => {
                return (
                    <p key={idx}>
                        |
                        <Link to={`/pets/${pet._id}`}>Name: {pet.name}</Link>
                        |
                        <p>Type: {pet.type}</p>
                        |
                        <Link to={`/pets/${pet._id}/edit`}>Edit</Link>
                        |
                        <DeleteButton petId={pet._id} removeFromDom={() => removeFromDom(pet._id)}>Adopt {pet.name}!</DeleteButton>
                    </p>
                )
            })}
        </div>
    )
}

export default PetList;