<template>
  <v-layout>

    <v-app-bar elevation="1" v-if="display.mdAndUp">

      <v-row>
        <v-col cols="1">

        </v-col>

        <v-col>
          <v-btn to="/" class="text-left">
            {{ appTitle }}
          </v-btn>

        </v-col>

        <v-col>
          <div v-if="authStore.token" class="text-right">
            <v-btn v-for="item in desktopWithAuth" :key="item.title" :to="item.path">
              {{ item.title }}
            </v-btn>
          </div>

          <div v-else>
            <v-btn v-for="item in desktopWithoutAuth" :key="item.title" :to="item.path">
              {{ item.title }}
            </v-btn>
          </div>

        </v-col>

        <v-col cols="1">

        </v-col>
      </v-row>
    </v-app-bar>



    <v-bottom-navigation v-else grow>
      <v-btn v-for="item in mobile" :key="item.title" color="teal" :to="item.path">
        <v-icon>{{ item.icon }}</v-icon>
        {{ item.title }}
      </v-btn>
    </v-bottom-navigation>



    <v-main>
      <v-row v-if="display.mdAndUp">
        <v-col cols="1">

        </v-col>

        <v-col>
          <router-view></router-view>
        </v-col>


        <v-col cols="1">

        </v-col>
      </v-row>


      <v-row v-else>
        <v-col cols="1">

        </v-col>

        <v-col>
          <router-view></router-view>
        </v-col>


        <v-col cols="1">

        </v-col>
      </v-row>
    </v-main>

  </v-layout>
</template>

<script>

import { useDisplay } from 'vuetify'
import { ref } from 'vue'
import { useAuthStore } from '@/store/auth';

export default {
  components: {

  },

  data() {
    const display = ref(useDisplay())
    const authStore = useAuthStore();

    return {
      appTitle: "Auto",
      desktopWithAuth: [
        { title: "거래 내역", path: "/record" },
        { title: "현재 거래 목록", path: "/in-progress" },
        { title: "내 설정", path: "/setting" },
        { title: "백테스트", path: "/backtest" },
        { title: "로그아웃", path: "/logout" }
      ],

      desktopWithoutAuth: [
        { title: "로그인", path: "/login" },
      ],


      mobile: [
        { title: "홈", path: "/", icon: "mdi-home-outline" },
        { title: "거래 내역", path: "/record", icon: "mdi-school-outline" },
        { title: "현재 거래 목록", path: "/in-progress", icon: "mdi-bullhorn-outline" },
        { title: "내 설정", path: "/setting", icon: "mdi-cog-outline" },

      ],
      display,
      authStore
    };
  },
}
</script>
