import axios from "axios"

const apiURL = axios.create({
    baseURL: "http://localhost:8000/myapp/api/"
})
export const ObtenerUsuarios = () => apiURL.get('/');

export const createUsuarios = (usuario) => apiURL.post('/', usuario);
