<template>
    <v-container fluid>
        <v-row>
            <v-col cols="2"></v-col>
            <v-col>

                <v-card elevation="0">
                    <v-img :src="richshrimp" max-height="500"></v-img>
                </v-card>
                <v-card>
                    <v-card-title>
                        <v-spacer></v-spacer>
                        <v-text-field v-model="upbitStore.search" append-icon="mdi-magnify" label="실시간 시세 보기"
                            single-line hide-details></v-text-field>
                    </v-card-title>
                    <v-data-table v-if="display.mdAndUp" :headers="upbitStore.headers" :items="upbitStore.coinInfo"
                        :search="upbitStore.search"></v-data-table>

                    <v-data-table v-else :headers="upbitStore.mobileHeaders" :items="upbitStore.coinInfo"
                        :search="upbitStore.search"></v-data-table>
                </v-card>
            </v-col>
            <v-col cols="2"></v-col>
        </v-row>

    </v-container>

</template>

<script>
import richshrimp from '../assets/img/logo.jpg'
import { useUpbitStore } from '../store/upbit.js'
import { ref } from 'vue'
import { useDisplay } from 'vuetify'
import { VDataTable } from 'vuetify/labs/VDataTable'

export default {
    name: 'HomeView',

    components: {
        VDataTable,
    },

    setup() {
        const upbitStore = useUpbitStore();

        upbitStore.getTicker();

        return {
            upbitStore
        }
    },

    data() {
        const display = ref(useDisplay());


        return {
            display,
            richshrimp
        }
    },

}
</script>