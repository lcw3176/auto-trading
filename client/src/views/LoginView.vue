<template>
    <v-container is-fluid>
        <v-sheet class="pa-12">
            <v-card class="mx-auto px-6 py-8" max-width="500" elevation="0" variant="outlined">
                <v-form ref="form" @submit.prevent="login">
                    <input type="hidden" name="contact_number">

                    <v-text-field label="id" variant="underlined" name="id" v-model="authStore.id">
                    </v-text-field>


                    <v-text-field label="password" variant="underlined" name="pw" v-model="authStore.pw"
                        type="Password">
                    </v-text-field>

                    <v-btn type="submit" color="success">로그인</v-btn>

                </v-form>
            </v-card>
        </v-sheet>


    </v-container>
</template>


<script>

import { useAuthStore } from '@/store/auth.js'

export default {

    components: {

    },

    setup() {
        const authStore = useAuthStore();

        return {
            authStore,
        }

    },


    methods: {
        login() {
            this.authStore.login();
        },
    }

}
</script>