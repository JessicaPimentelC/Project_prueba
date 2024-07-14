import { Link } from "react-router-dom";

export function Navigation(){
    return(
<div>
    <Link to="/usuario-create">Crear usuario</Link>
    <Link to="/usuario">usuarios</Link>
</div>

    )
}