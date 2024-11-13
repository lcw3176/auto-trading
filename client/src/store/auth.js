import { defineStore } from "pinia";
import axios from 'axios';

async function requsetAuth(params) {
    try {
        const response = await axios.get('http://localhost:8000/v1/ticker', { params });

        return response.data;
    } catch (error) {
        console.error(error);
        return [];
    }

}


export const useAuthStore = defineStore("auth", {

    state: () => ({
        token : "asdasd",
    }),


    getters: {

    },

    actions: {
        
  

    },
});