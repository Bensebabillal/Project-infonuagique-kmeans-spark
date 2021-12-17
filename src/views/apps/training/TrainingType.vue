<template>
    <div>
        <div class="flex items-center   mb-2">
            <div class="ml-auto">
                <vs-avatar class="m-0" :src="this.training_type.image"
                           size="45px"></vs-avatar>
            </div>
            <div class="ml-4 mr-auto">
                <h4 style="font-weight: 700;">{{ name }}</h4>

            </div>
        </div>
        <p class="text-center"> {{ description }}
        </p>


        <div class="mt-5">


            <!-- left -->

            <template v-if="training_sessions.length===0">

                <div class="items-grid-view vx-row ">
                    <div v-for="(index) in 6" :key="index"
                         class="vx-col  lg:w-1/3 sm:w-1/2 w-full">

                        <vx-card
                                class="card-overlay bg-cover mt-5"
                                style="border-radius: .5rem !important;"

                        >
                            <vue-content-loading v-bind="$attrs" :width="300" :height="225">
                                <rect x="0" y="0" rx="3" ry="3" width="300" height="170"/>
                                <!--                                    <rect x="0" y="180" rx="2" ry="2" width="35" height="45"/>-->
                                <rect x="0" y="180" rx="2" ry="2" width="150" height="15"/>
                                <rect x="0" y="203" rx="2" ry="2" width="100" height="10"/>
                            </vue-content-loading>
                        </vx-card>
                    </div>
                </div>

            </template>

            <template v-else>

                <div class="items-grid-view vx-row mt-5">

                    <div class="vx-col lg:w-1/3 sm:w-1/2 w-full" v-for="item in training_sessions" :key="item.id">

                        <item-grid-view :item="item">

                            <!-- SLOT: ACTION BUTTONS -->
                            <template slot="action-buttons">
                                <div class="flex flex-wrap" @click="navigate_to_detail_view(item.id)">


                                    <!-- SECONDARY BUTTON: ADD-TO/VIEW-IN CART -->
                                    <div
                                            class="item-view-secondary-action-btn bg-primary p-3 flex flex-grow items-center justify-center text-white cursor-pointer"
                                    >
                                        <feather-icon icon="PlayCircleIcon" svgClasses="h-4 w-4"/>


                                        <span class="text-sm font-semibold ml-2">Watch this Session</span>
                                    </div>
                                </div>
                            </template>
                        </item-grid-view>

                    </div>
                </div>


            </template>


        </div>


    </div>
</template>

<script>

    import {getAPI} from "@/axios";
    import {VueContentLoading} from 'vue-content-loading'

    export default {
        components: {
            ItemGridView: () => import('./components/ItemGridView.vue'),
            VueContentLoading
        },

        data() {
            return {

                training_sessions: [],
                training_type: {},
                name: "",
                description: "",
                Level: 1,
                id: null


            }
        },
        computed: {
            toValue() {
                return (value, range) => [
                    value.min !== null ? value.min : range.min,
                    value.max !== null ? value.max : range.max
                ]
            },


            windowWidth() {
                return this.$store.state.windowWidth
            }
        },
        watch: {
            windowWidth() {
                this.setSidebarWidth()
            }
        },
        methods: {
            navigate_to_detail_view(session) {
                this.$router.push({
                    name: 'training-Session',
                    query: {training_session: this.$route.params.slug, session: session}
                })
                    .catch(() => {
                    })
            },
            getSessions() {
                console.log(this.$route.params.slug)
                getAPI.get('player/api/v1/program/training-session/?training_session=' + this.$route.params.slug,
                ).then(response => {
                    // commit('offerPosts', response.data)
                    setTimeout(() => {
                        console.log("World!");
                    }, 2000);
                    console.log('i am here')
                    console.log(response.data['results'][0].sessions)
                    this.training_sessions.push(...response.data['results'][0].sessions);
                    this.training_type = response.data['results'][0].training_types;
                    this.description = response.data['results'][0].description;
                    this.level = response.data['results'][0].level;
                    this.name = response.data['results'][0].name;
                    // console.log(response.data);
                }).catch(error => {
                    console.log('i am here error ')
                    console.log(error);
                    // commit('showErrorAlert', error.data)
                    // console.log(error.response.data);
                })
            },

            setSidebarWidth() {
                if (this.windowWidth < 992) {
                    this.isFilterSidebarActive = this.clickNotClose = false
                } else {
                    this.isFilterSidebarActive = this.clickNotClose = true
                }
            },

            // GRID VIEW - ACTIONS
            toggleFilterSidebar() {
                if (this.clickNotClose) return
                this.isFilterSidebarActive = !this.isFilterSidebarActive
            },


        },
        created() {
            this.setSidebarWidth()
        },
        mounted() {
            this.getSessions()
        },
    }
</script>
<style>
    .vx-card {
        background: #fff;
        border-radius: 1.5rem;
        box-shadow: 0px 4px 25px 0px rgba(0, 0, 0, 0.1);
    }

    .vs-tabs-position-left .activeChild button {
        background-color: black;
        border-radius: 10px;
    }

    .ps {
        height: 80vh;
    }
</style>
