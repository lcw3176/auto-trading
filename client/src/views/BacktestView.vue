<template>
    <v-app>
        <v-overlay :value="isLoading" absolute>
            <v-spinner size="64" color="primary" />
            <v-alert :value="isLoading" type="info" prominent>
                차트 로딩중입니다
            </v-alert>
        </v-overlay>

        <v-container>
            <v-form ref="dataForm" v-on:submit.prevent="startBacktest">
                <v-row>
                    <v-col cols="2">

                    </v-col>

                    <v-col cols="8">
                        <v-form>
                            <v-autocomplete v-model="formData.ticker" :items="backtestStore.coins" label="거래할 종목을 선택해주세요"
                                variant="solo" required clearable />

                            <v-text-field v-model="formData.startBalance" label="시작 원화 잔고" type="number" variant="solo"
                                required />

                            <v-text-field v-model="formData.maxAdditionalBuyCount" label="최대 추가 매수 횟수를 입력해주세요"
                                type="number" placeholder="단일 매수시 0 입력" variant="solo" required />

                            <v-select v-model="formData.strategyType" :items="backtestStore.strategies" variant="solo"
                                item-value="strategy" label="사용 전략" required clearable />

                            <v-select v-model="formData.candleMinute" :items="backtestStore.candleMinutes" variant="solo" label="기준 분봉" required clearable />

                            <v-text-field v-model="formData.startDate" label="시작 날짜" type="datetime-local"
                                variant="solo" required  />
                            <v-text-field v-model="formData.endDate" label="종료 날짜" type="datetime-local" variant="solo"
                                required />
                            <v-text-field v-model="backtestResult" label="예상 이득" readonly />
                            <v-col>
                                <v-btn @click="startBacktest" color="primary">시작</v-btn>
                            </v-col>
                        </v-form>

                    </v-col>


                    <v-col cols="2">

                    </v-col>



                </v-row>
            </v-form>

            <!-- 차트 -->
            <v-row>
                <v-col cols="2">

                </v-col>
                <v-col cols="8">
                    <div id="chart" style="height: 700px; width: 100%;"></div>
                </v-col>
                <v-col cols="2">
                    
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<script>
import { ref } from 'vue';
import { useBacktestStore } from '@/store/backtest.js'

const socket = new WebSocket('ws://localhost:8000/backtest');


export default {
    name: 'BacktestForm',
    setup() {
        const backtestStore = useBacktestStore();
        backtestStore.requestInitData();

        const isLoading = ref(false);
        const formData = ref({
            ticker: '',
            startBalance: '',
            maxAdditionalBuyCount: 0,
            strategyType: '',
            candleMinute: '',
            startDate: '',
            endDate: '',
        });
        const backtestResult = ref('');


        let isRun;
        let markers = [];
        let chart = '';
        let candleSeries = '';


        const startBacktest = () => {
            if (!isLoading.value) {
                isLoading.value = true;
                socket.send(JSON.stringify(formData.value));
            }
        };


        return {
            formData,
            backtestResult,
            isLoading,
            startBacktest,
            isRun,
            markers,
            chart,
            candleSeries,
            socket,
            backtestStore
        };
    },


    mounted() {

        this.isRun = true;
        this.markers = [];
        this.chart = LightweightCharts.createChart(document.getElementById("chart"), {
            localization: {
                dateFormat: 'yyyy-MM-dd',
                locale: 'ko-KR'
            },

            timeScale: {
                timeVisible: true,
                secondsVisible: true,
                minBarSpacing: 0.05,
                barSpacing: 12
            },
        });



        this.candleSeries = this.chart.addCandlestickSeries();


        const update = (value) => {
            if (value.finish) {
                isLoading.value = false;
                backtestResult.value = value.gain;
                return;
            }

            let currentBar = {
                open: value.open,
                high: value.high,
                low: value.low,
                close: value.close,
                time: value.time
            };


            this.candleSeries.update(currentBar)

            if (value.traded) {

                if (value.buy) {
                    this.markers.push({
                        time: Date.parse(value.time) / 1000 + 32400,
                        position: 'belowBar',
                        color: '#2196F3',
                        shape: 'arrowUp',
                        text: 'Buy: ' + value.tradedPrice
                    });

                } else {
                    this.markers.push({
                        time: Date.parse(value.time) / 1000 + 32400,
                        position: 'aboveBar',
                        color: '#e91e63',
                        shape: 'arrowDown',
                        text: 'Sell: ' + value.tradedPrice
                    });
                }

                this.candleSeries.setMarkers(this.markers);
            }
        };

        this.socket.onmessage = function (event) {
            update(JSON.parse(event.data));
        };


    }
};
</script>

<style scoped>
#chart {
    height: 600px;
}
</style>