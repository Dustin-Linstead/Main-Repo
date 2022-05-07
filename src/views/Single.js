import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, navigate } from '@reach/router';
import DeleteButton from '../components/DeleteButton';

const OnePet = props => {
    const { id } = props;
    const [pet, setPet] = useState({});
    const [error, setErrors] = useState()


    useEffect(() => {
        axios.get(`http://localhost:8000/api/pets/${id}`)
            .then(res => {
                setPet(res.data.results)
                setErrors(res.data.results)
            })
            .catch(err => navigate('/pets'))
        
    }, [])

    return(
        <div>
            <p>Name: {pet.name}</p>
            <p>Type: {pet.type}</p>
            <p>Description: {pet.description}</p>
            <p>Skill1: {pet.skill1}</p>
            <p>Skill2: {pet.skill2}</p>
            <p>Skill3: {pet.skill3}</p>
            <Link to={`/pets/${pet._id}/edit`}>Edit</Link><br/>
        </div>
        
    )
}

export default OnePet