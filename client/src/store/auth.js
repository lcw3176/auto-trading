import { defineStore } from "pinia";
import axios from 'axios';
import router from "@/router";
import Cookies from 'js-cookie';

const api = axios.create({
    timeout: 10000
});

const baseUrl = process.env.VUE_APP_HOST_URL;

api.interceptors.response.use((response) => response, (error) => {
    alert(error);
    throw error;
});


async function requsetLogin(id, pw) {
    const response = await api.post(baseUrl + '/login', {
        "id": id,
        "pw": pw
    }, {
        withCredentials: true,
    });

    return response;
}


export const useAuthStore = defineStore("auth", {

    state: () => ({
        token: Cookies.get('token'),
        id: "",
        pw: "",
    }),


    getters: {

    },

    actions: {

        async login() {
            let response = await requsetLogin(this.id, this.pw);
            
            if(response.status === 200){
                this.token = Cookies.get('token');
                await router.push("/home");
            }
            
        },

        async logout(){
            this.token = "";
            Cookies.remove('token');
            await router.push("/home");
        }

    },
});