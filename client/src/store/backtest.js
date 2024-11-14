import { defineStore } from "pinia";
import axios from 'axios';

const api = axios.create({
    timeout: 10000
});

const baseUrl = process.env.VUE_APP_HOST_URL;

api.interceptors.response.use((response) => response, (error) => {
    alert(error);
    throw error;
});


async function requsetBacktestInfo() {
    const response = await api.get(baseUrl + '/backtest');

    return response;
}


export const useBacktestStore = defineStore("backtest", {

    state: () => ({
        coins: [],
        strategies: ['A', 'B'],
        candleMinutes: [],

    }),


    getters: {

    },

    actions: {

        async requestInitData(){
           const response = await requsetBacktestInfo();
            
           if(response.status === 200){
                this.coins = response.data.ticker;
                this.candleMinutes = response.data.candle_minute;
           }
        }

    },
});