import React, { useState } from 'react';
import PetForm from '../components/Form';
import { navigate } from '@reach/router';
import axios from 'axios';

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
    description: ''
}

const NewPet = () => {
    const [pet, setPet] = useState(initialPet);
    const [errors, setErrors] = useState(initialErrors);

    const changeHandler = e => {
        setPet({ ...pet, [e.target.name]: e.target.value })
    }

    const submitHandler = e => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/pets', pet)
            .then(res => {
                const { message, results } = res.data;
                if (message === "success") {
                    navigate(`/pets/${results._id}`)
                } else {
                    console.log(res)
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
            <PetForm
                pet={pet}
                errors={errors}
                submitHandler={submitHandler}
                changeHandler={changeHandler}
                action="Submit"
            />
        </div>
    )
}

export default NewPet