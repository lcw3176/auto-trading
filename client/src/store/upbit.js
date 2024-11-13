import { defineStore } from "pinia";
import axios from 'axios';

async function requsetTicker(params) {
    try {
        const response = await axios.get('https://api.upbit.com/v1/ticker', { params });

        return response.data;
    } catch (error) {
        console.error(error);
        return [];
    }

}


async function requestAllMarkets() {
    try {
        const response = await axios.get('https://api.upbit.com/v1/market/all');

        return response.data;
    } catch (error) {
        console.error(error);
        return [];
    }
}


export const useUpbitStore = defineStore("upbit", {

    state: () => ({
        markets : [],
        coinInfo : [],
        search: '',

        headers: [
            {
              key: 'market',
              title: '코드',
            },
            { key: 'koreanName', title: '이름' },
            { key: 'tradePrice', title: '가격' }
          ],

        mobileHeaders: [
            { key: 'koreanName', title: '이름' },
            { key: 'tradePrice', title: '가격' }
        ],
    }),


    getters: {

    },

    actions: {
        
        // 코인 종류를 가져온다
        async setMarkets(){
            let data = await requestAllMarkets();

            for(let i of data){
                this.markets.push({
                    market: i.market,
                    korean: i.korean_name,
                    english: i.english_name,
                });
            }
        },


        // 현재가 정보를 불러온다.
        async getTicker() {
            
            if(this.markets.length == 0){
                await this.setMarkets();
            }

            let data = await requsetTicker({
                markets: this.markets.map(function(v){
                    return v.market;
                }).join()
            });
            
            this.coinInfo.length = 0;
            
            for(let i of data){
                this.coinInfo.push({
                    market : i.market,
                    tradePrice : i.trade_price,
                    koreanName : this.markets.find(function(e){
                        return e.market === i.market;
                    }).korean,
                })
            }
            
        }

    },
});