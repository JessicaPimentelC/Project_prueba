import { useForm } from 'react-hook-form';

export function UsuarioPage(){
    const {register, handleSubmit} = useForm();
    
    const onSubmit = handleSubmit(data => {
        console.log(data)
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