<template>
    <v-container fluid>
        <v-card>
        <v-card-title>
            <v-spacer></v-spacer>
            <v-text-field v-model="upbitStore.search" append-icon="mdi-magnify" label="검색하기" single-line
                hide-details></v-text-field>
        </v-card-title>
        <v-data-table v-if="display.mdAndUp" :headers="upbitStore.headers" :items="upbitStore.coinInfo"
            :search="upbitStore.search"></v-data-table>

        <v-data-table v-else :headers="upbitStore.mobileHeaders" :items="upbitStore.coinInfo"
            :search="upbitStore.search"></v-data-table>
    </v-card>
    </v-container>
   
</template>
  
<script>
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
            display
        }
    },

}
</script>