<!-- =========================================================================================
    File Name: Login.vue
    Description: Login Page
    ----------------------------------------------------------------------------------------
    Item Name: Vuexy - Vuejs, HTML & Laravel Admin Dashboard Template
      Author: Pixinvent
    Author URL: http://www.themeforest.net/user/pixinvent
========================================================================================== -->


<template>
    <div class="h-screen flex w-full  vx-row no-gutter items-center justify-center"
         style="background-color: #f8f8f8; overflow: hidden"
         id="page-login">
        <div class="vx-col flex w-full" style=" min-height: 101vh;">


            <vs-row vs-align="center"
                    vs-type="flex" vs-justify="center" class="no-gutter"
                    style="justify-content: space-between ;">

                <div style=" max-height: 101vh;" class="vx-col flex items-center hidden lg:block lg:w-2/3 xl:3/4">
                    <!--                    <img src="@/assets/images/pages/login/foot-back.png" class="mx-auto"/>-->
                    <img src="@/assets/images/pages/login/foot-back.jpg" alt="login" class="mx-auto"
                         style="height: 1200px;">
                    <!--                            <img v-if="smallScreen() === false" src="@/assets/images/pages/login/foot-back.png"-->
                    >
                </div>

                <div class="vx-col w-full center-card-log  sm:w-full md:w-full lg:w-1/3 xl:1/4"
                     :style="themeMode?' background-color: rgba(40, 48, 70, 0.97)':'background-color:white'"
                     style=" z-index: 2;   min-height: 101vh; padding-bottom: 6rem; border-left: 1px solid #262c49; ">
                    <div class="px-8 pt-8 mx-auto" style="">
                        <div>


                            <router-link tag="div" class=" mb-10 vx-logo cursor-pointer flex items-center"
                                         to="/">
                                <logo class="ml-auto  w-25 mr-4 fill-current text-primary"/>
                                <span class="  mr-auto vx-logo-text "
                                      :class="themeMode?'text-white':'text-dark'"
                                      style="font-size: 35px;"
                                >ChicagoCrime </span>
                            </router-link>

                            <!--                                <div class="mr-auto  ml-auto ">-->
                            <!--                                    <h1 class="mr-auto  ml-auto mb-8" style="text-align: center; font-size: 50px">-->
                            <!--                                        Fox Sportif</h1>-->
                            <!--                                </div>-->

                            <!--                                <span class="vx-logo-text text-primary">Fox Sportif</span>-->
                            <div class="vx-card__title mb-10" style="text-align: center">
                                <h4 class="mb-4">Connexion</h4>
                                <p>Log in to see today's training 😊</p>
                            </div>


                            <login-jwt></login-jwt>
                        </div>
                    </div>
                </div>
            </vs-row>

        </div>
    </div>
</template>


<script>
    import LoginJwt from './LoginJWT.vue'
    import Logo from '../../../layouts/components/Logo'


    export default {
        components: {
            LoginJwt,
            Logo
        },
        methods: {
            smallScreen() {
                return window.width < 800;
            }
        },
        computed: {
            themeMode: {
                get() {
                    return this.$store.state.theme === "dark" ? true : false;
                },

            },
        }
    }
</script>

<style lang="scss">
    .center-card-log {
        justify-content: center;
        display: flex;
        align-items: center;
    }

    .login-tabs-container {
        min-height: 505px;

        .con-tab {
            padding-bottom: 14px;
        }

        .con-slot-tabs {
            margin-top: 1rem;
        }
    }

    .hidden {
        display: none;
    }

</style>
