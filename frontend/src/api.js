import axios from "axios";

const API_URL = "http://localhost:9000/animal"; 

export const fetchItems = () => axios.get(API_URL);

export const createItem = (item) => {const formData = new FormData();
                                    formData.append('kind', item.kind);
                                    formData.append('name', item.name);
                                    formData.append('age', item.age);
                                    return axios.post(API_URL, formData);}
                                    
export const updateItem = (item) => axios.put(`${API_URL}/${item.id}`, item);
export const deleteItem = (id) => axios.delete(`${API_URL}/${id}`);
