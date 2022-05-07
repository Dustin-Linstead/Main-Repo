import { React, useState, useEffect } from 'react';
import axios from 'axios';
import PetList from '../components/PetList'


const AllPets = () => {
    const [pets, setPet] = useState([]);
    const [loaded, setLoaded] = useState(false)
    useEffect(() => {
        axios.get('http://localhost:8000/api/pets')
            .then(res => {
                setPet(res.data.results)
                setLoaded(true);
            })
            .catch(err => console.log(err))
    }, [])

    const removeFromDom = petId => {
        setPet(pets.filter(pet => pet._id !== petId));
    }

    return (
        <div>
            {loaded && <PetList pets={pets} removeFromDom={removeFromDom}/>}
            <hr/>
        </div>
        
    )
}

export default AllPets