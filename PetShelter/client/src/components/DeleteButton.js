import React from 'react'
import axios from 'axios';
import { navigate } from '@reach/router';

const DeleteButton = props => {
    const { petId, removeFromDom } = props;
    const deleteHandler = e => {
        axios.delete(`http://localhost:8000/api/pets/` + petId)
            .then(res => {
                removeFromDom();
                navigate('/pets')})
            .catch(err => navigate('/pets'));
    }
    return (
        <input type="button" value="Adopt" className="col-sm-2" onClick={deleteHandler}/>
    )
}

export default DeleteButton