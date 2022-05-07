import React from 'react';
import { navigate } from '@reach/router';

const PetForm = props => {
    const { submitHandler, pet, changeHandler, action, DeleteButton, errors} = props;

    return(
        <form className="col-sm-12" onSubmit={submitHandler}>
            <div className="form-group row">
                {
                    errors.name ?
                    <span>{errors.name}</span>
                    :
                    ''
                }
                <label htmlFor="name" className="col-sm-4">Pet Name: </label>
                <input type="text" name="name" className="col-sm-8" onChange={changeHandler} value={pet.name}/>
            </div>
            <div className="form-group row">
                {
                    errors.type ?
                    <span className="col-sm-8 text-danger offset-sm-4">{errors.type}</span>
                    :
                    ''
                }
                <label htmlFor="type" className="col-sm-4">Pet Type: </label>
                <input type="text" name="type" className="col-sm-8" onChange={changeHandler} value={pet.type}/>
            </div>
            <div className="form-group row">
                {
                    errors.description ?
                    <span className="col-sm-8 text-danger offset-sm-4">{errors.description}</span>
                    :
                    ''
                }
                <label htmlFor="description" className="col-sm-4">Description: </label>
                <input type="text" name="description" className="col-sm-8" onChange={changeHandler} value={pet.description}/>
            </div>
            <div className="form-group row">
                <label htmlFor="skills" className="col-sm-4">Skills (Optional)</label>
                <input type="text" name="skill1" className="col-sm-8" onChange={changeHandler} value={pet.skill1}/><br/>
                <input type="text" name="skill2" className="col-sm-8" onChange={changeHandler} value={pet.skill2}/><br/>
                <input type="text" name="skill3" className="col-sm-8" onChange={changeHandler} value={pet.skill3}/><br/>
            </div>
            <div className="form-group row flex-right">
                {
                    DeleteButton ?
                    DeleteButton
                    :
                    ''
                }
                <input type="button" className="col-sm-2" value="Cancel" onClick={ () => navigate('/pets')}/>
                <input type="submit" className="col-sm-2" value={action}/>
            </div>
        </form>
    )
}

export default PetForm