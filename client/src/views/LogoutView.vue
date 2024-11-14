<template>
    <v-container is-fluid>
        로그아웃...

    </v-container>
</template>


<script>

import { useAuthStore } from '@/store/auth.js'

export default {

    components: {

    },

    setup() {
        const authStore = useAuthStore();
        authStore.logout();
    },


}
</script>