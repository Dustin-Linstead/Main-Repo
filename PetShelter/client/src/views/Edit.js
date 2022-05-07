import React, { useState, useEffect } from 'react';
import PetForm from '../components/Form';
import axios from 'axios';
import { navigate } from '@reach/router';
import DeleteButton from '../components/DeleteButton';

const initialPet = {
    name: '',
    type: '',
    description: '',
    skills1: '',
    skills2: '',
    skills3: ''
}
const initialErrors = {
    name: '',
    type: '',
    description: '',

}

const EditPet = props => {
    const { id } = props;
    const [pet, setPet] = useState(initialPet);
    const [errors, setErrors] = useState(initialErrors);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/pets/`+ id)
            .then(res => {
                setPet(res.data.results)
            })
            .catch(err => navigate('/pets'))

    }, []);

    const changeHandler = e => {
        setPet({ ...pet, [e.target.name]: e.target.value })
    }

    const submitHandler = e => {
        e.preventDefault();
        axios.put(`http://localhost:8000/api/pets/${id}`, pet)
            .then(res => {
                const { message, results } = res.data;
                if (message === "success") {
                    navigate(`/pets/${results._id}`)
                } else {
                    const newErrors = { ...initialErrors };
                    for (const key in results.errors) {
                        newErrors[key] = results.errors[key].message;
                    }
                    setErrors(newErrors);
                }
            })
    }
    return (
        <div className="col-sm-12">
            <h2> Edit Pet </h2>
            <PetForm
                pet={pet}
                errors={errors}
                submitHandler={submitHandler}
                changeHandler={changeHandler}
                action="Update"
                DeleteButton={<DeleteButton id={id}>Adopt</DeleteButton>}
            />
        </div>
    )
}

export default EditPet