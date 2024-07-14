import { useForm } from 'react-hook-form';
import { createUsuarios } from '../api/Usuario-api';


export function UsuarioFormPage(){
    const {register, handleSubmit} = useForm();
    
    const onSubmit = handleSubmit(async data => {
        
        const res = await createUsuarios(data)
        console.log(res)
    })
    return (
        <div>
            <form onSubmit={onSubmit}>
            <input type="email" placeholder="Email" {...register("email",{required: true})} />
            <input type="text" placeholder="Username" {...register("Username",{required: true})} />
            <input type="password" placeholder="Password"{...register("Password",{required: true})} />
            <button>save</button>

            </form>


        </div>
    )
}