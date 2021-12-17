<template>
    <div class="vx-row" :style="this.width?'margin: 0 -2rem;':''">
        <template v-if="trainingExercise.length===0">    <!-- COL 2 -->
            <div class="vx-col w-full lg:w-3/4 mb-2">

                <div>
                    <!-- POST HEADER -->
                    <div class="post-header flex justify-between ">
                        <div class="flex items-center">
                            <vue-content-loading v-bind="$attrs" :width="300" :height="30">
                                <rect x="0" y="0" rx="2" ry="2" width="150" height="15"/>
                                <rect x="0" y="20" rx="2" ry="2" width="100" height="10"/>
                            </vue-content-loading>
                        </div>


                    </div>


                    <div class="post-media-container  mt-4">
                        <ul class="flex post-media-list">
                            <li class="post-media w-full">
                                <vue-content-loading v-bind="$attrs" :width="300" :height="225">
                                    <rect x="0" y="0" rx="3" ry="3" width="300" height="170"/>
                                    <!--                                    <rect x="0" y="180" rx="2" ry="2" width="35" height="45"/>-->
                                    <rect x="0" y="180" rx="2" ry="2" width="150" height="15"/>
                                </vue-content-loading>
                                <!--                                <span class="text-lg text-primary" v-else>Unknown Media Type</span>-->
                            </li>

                        </ul>
                        <!--                    <span class="flex justify-end" v-if="trainingExercise[selectExercise].media.length > 2">-->
                        <!--                                <a class="inline-flex items-center text-sm" href=""><span>View All</span> <feather-icon-->
                        <!--                                        :icon="$vs.rtl ? 'ChevronsLeftIcon' : 'ChevronsRightIcon'"-->
                        <!--                                        svgClasses="h-4 w-4"></feather-icon></a>-->
                        <!--                            </span>-->
                    </div>


                </div>

            </div>
            <div class="vx-col w-full lg:w-1/4 ">
                <vx-card class="">
                    <div>
                        <!-- POST HEADER -->
                        <div class="post-header flex justify-between mb-4">
                            <div class="flex items-center">
                                <div>
                                    <vs-avatar class="m-0"
                                               color="primary"

                                               :src="require('@/assets/images/training/fitness_center-white-48dp.svg')"
                                               size="40px"></vs-avatar>
                                </div>
                                <div class="ml-4">

                                    <h4>Exercises</h4>

                                </div>

                            </div>


                        </div>

                        <div class="flex flex-wrap">

                            <div

                                    class="w-full  mb-4">
                                <vue-content-loading v-bind="$attrs" :width="300" :height="225">
                                    <rect x="0" y="0" rx="2" ry="2" width="300" height="50"/>
                                    <rect x="0" y="60" rx="2" ry="2" width="300" height="50"/>
                                    <rect x="0" y="120" rx="2" ry="2" width="300" height="50"/>
                                    <rect x="0" y="180" rx="2" ry="2" width="300" height="50"/>
                                </vue-content-loading>
                            </div>


                        </div>


                    </div>
                </vx-card>
            </div>

        </template>

        <template v-else>
            <!-- COL 2 -->
            <div class="vx-col w-full lg:w-3/5 mb-2">

                <div>
                    <!-- POST HEADER -->
                    <div class=" post-header flex justify-between mb-4"
                         :style="this.windowWidth < 990?'margin-right: 0':'margin-left: 10px'">
                        <div class="flex items-center mr-auto ml-auto">
                            <div>
                                <vs-avatar class="m-0" :src="training_type.image"
                                           size="45px"></vs-avatar>
                            </div>
                            <div class="ml-4">
                                <h2 class="te">{{training_type.name}}</h2>
                                <h6 style="color: #959ea9">{{ name }} - {{ week }}/{{ day_in_week }}</h6>

                            </div>
                        </div>


                    </div>


                    <div class="post-media-container mb-6 mt-4"
                         v-sticky="{ zIndex: 4444, stickyTop: 60}"
                         :style="this.windowWidth < 990?'margin-right: 0':'margin-left: 10px'"
                    >
                        <div>
                            <ul class="flex post-media-list">
                                <li class="post-media w-full">
                                    <!--                            <img class="responsive rounded" :src="trainingExercise[selectExercise].video" alt="user-upload"-->
                                    <!--                                 v-if="mediaType(media) === 'image'">-->

                                    <video-player
                                            :playsinline="true"
                                            ref="player"
                                            class="media-video-player"
                                            :options="playerOptions(
                                                {
                                                      sources: [{type: 'video/mp4', src: trainingExercise[selectExercise].video}],
                                                      poster: trainingExercise[selectExercise].image})"

                                    />
                                    <!--                                <span class="text-lg text-primary" v-else>Unknown Media Type</span>-->
                                </li>
                            </ul>
                        </div>

                        <!--                    <span class="flex justify-end" v-if="trainingExercise[selectExercise].media.length > 2">-->
                        <!--                                <a class="inline-flex items-center text-sm" href=""><span>View All</span> <feather-icon-->
                        <!--                                        :icon="$vs.rtl ? 'ChevronsLeftIcon' : 'ChevronsRightIcon'"-->
                        <!--                                        svgClasses="h-4 w-4"></feather-icon></a>-->
                        <!--                            </span>-->
                    </div>
                    <vs-row class="mt-2 mb-5">
                        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="5">

                            <vs-button v-if="this.selectExercise === 0" disabled style="width: 50%">Previous</vs-button>
                            <vs-button v-else style="width: 50%" @click="precExercise">Previous</vs-button>
                        </vs-col>
                        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                            <vs-button radius color="primary" type="border" icon-pack="feather"
                                       icon="icon-repeat" @click="replayVideo"></vs-button>
                        </vs-col>
                        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="5">
                            <!--                            <vs-button style="width: 50%" >Next</vs-button>-->
                            <vs-button style="width: 50%" @click="nextExercise">Next</vs-button>
                        </vs-col>
                    </vs-row>
                    <!-- CHART DATA -->
                    <!-- Support Tracker Meta Data -->
                    <h3 class="ml-5  text-success" style="font-weight: 600;">
                        {{trainingExercise[selectExercise].name}}</h3>
                    <div class="ml-2 mr-2 mt-5">
                        <vx-card class="mr-auto ml-auto" id="padding-card-resize">
                            <div class="flex flex-row justify-between px-8 mt-2">

                                <p class="text-center">
                                    <span class="block">Repetition</span>
                                    <span class="text-2xl font-semibold">{{trainingExercise[selectExercise].number_of_repetition}}</span>
                                </p>
                                <p class="text-center">
                                    <span class="block">Set</span>
                                    <span class="text-2xl font-semibold">{{trainingExercise[selectExercise].number_of_set}}</span>
                                </p>
                                <p class="text-center">
                                    <span class="block">Rest time</span>
                                    <span class="text-2xl font-semibold">{{trainingExercise[selectExercise].rest_time.slice(3)}} s</span>
                                </p>
                            </div>
                        </vx-card>
                    </div>


                    <!--                <vx-card class="mt-5" title="Description" title-color="success"-->
                    <!--                         card-background="rgba(0, 0, 0, 0)"-->
                    <!--                         no-shadow-->
                    <!--                         collapse-action>-->
                    <!--                    <p class="mb-3">You can create Description content-->

                    <!--                    </p>-->
                    <!--                    <p class="mb-3">You can also put any actions or indication about the exercise </p>-->

                    <!--                </vx-card>-->
                    <vs-collapse>
                        <vs-collapse-item icon-arrow="arrow_downward" :open="true">
                            <div slot="header" class="text-success">
                                Description
                            </div>
                            <p class="mb-3">
                                {{trainingExercise[selectExercise].description}}
                            </p>

                        </vs-collapse-item>
                    </vs-collapse>
                </div>

            </div>
            <div class="vx-col w-full lg:w-2/5 " :style="this.windowWidth < 990?'margin: 0 0.6rem;':''">
                <vx-card class="" :style="this.windowWidth < 990?'margin-top: 0':'margin-top: 60px'">
                    <div>
                        <!-- POST HEADER -->
                        <div class="post-header flex justify-between mb-4">
                            <div class="flex items-center">
                                <div>
                                    <vs-avatar class="m-0"
                                               color="primary"

                                               :src="require('@/assets/images/training/fitness_center-white-48dp.svg')"
                                               size="40px"></vs-avatar>
                                </div>
                                <div class="ml-4">

                                    <h4>Exercises</h4>

                                </div>

                            </div>


                        </div>

                        <div class="flex flex-wrap">
                            <div style="border-radius: 10px" v-for="(exercise,index) in trainingExercise" :key="index"
                                 @click="selectExercise=index"
                                 :class="exercise.name !== trainingExercise[selectExercise].name ? 'w-full  mb-4 bg-grid-color' : 'w-full  mb-4 bg-grid-color-success'">
                                <span class="center-hor m-auto">{{exercise.name}}</span>
                            </div>


                        </div>


                    </div>
                </vx-card>
            </div>
        </template>

    </div>
</template>

<script>
    // require styles
    import 'video.js/dist/video-js.css'
    import {videoPlayer} from 'vue-video-player'
    import {getAPI} from "@/axios";
    import {VueContentLoading} from 'vue-content-loading'
    import VueSticky from 'vue-sticky'

    export default {
        directives: {
            'sticky': VueSticky,
        },
        components: {
            videoPlayer,
            VueContentLoading
        },
        name: "TrainingSession",
        data() {
            return {
                selectExercise: 0,
                mediaExtensions: {
                    img: ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'exif', 'tiff'],
                    video: ['avi', 'flv', 'wmv', 'mov', 'mp4', '3gp']
                },

                trainingExercise: [],

                width: true,
                training_type: {},
                name: "",
                week: "",
                day_in_week: "",
                time_in_day: "",
                id: null


            }
        },
        watch: {
            windowWidth() {
                this.setSidebarWidth()
            },
            selectExercise: function (val) {

            }
        },
        methods: {
            replayVideo() {

            },
            nextExercise() {
                this.selectExercise++
            },
            precExercise() {
                this.selectExercise--
            },

            setSidebarWidth() {
                this.width = this.windowWidth < 992;
            },
            getSessions() {


                getAPI.get('player/api/v1/program/training-exercise/?training_session=' + this.$route.query.training_session + '&training_exercise=' + this.$route.query.session).then(response => {
                    // commit('offerPosts', response.data)
                    setTimeout(() => {
                        console.log("World!");
                    }, 2000);
                    console.log(response.data['results'])
                    this.trainingExercise.push(...response.data['results'][0].exercises)

                    this.training_type = response.data['results'][0].training_type
                    this.name = response.data['results'][0].name
                    this.week = response.data['results'][0].week
                    this.day_in_week = response.data['results'][0].day_in_week
                    // console.log(this.trainingExercise);
                }).catch(error => {
                    console.log(error);
                    // commit('showErrorAlert', error.data)
                    // console.log(error.response.data);
                })
            }
        },
        mounted() {
            console.log('this is current videojs instance object', this.myVideoPlayer)

            this.getSessions()
        },
        computed: {
            player() {
                return this.$refs.videoPlayer.player
            },
            mediaType() {
                return (media) => {
                    if (media.img) {
                        const ext = media.img.split('.').pop()
                        if (this.mediaExtensions.img.includes(ext)) return 'image'
                    } else if (media.sources && media.poster) {
                        // other validations
                        return 'video'
                    }
                }
            },
            windowWidth() {
                return this.$store.state.windowWidth
            },
            playerOptions() {
                return (media) => {
                    return {
                        height: '300',
                        fluid: true,
                        autoplay: false,
                        muted: true,
                        loop: true,
                        language: 'en',
                        playbackRates: [0.7, 1.0, 1.5, 2.0],
                        sources: media.sources,
                        poster: media.poster
                    }
                }
            }
        },

    }
</script>

<style>

    #padding-card-resize .vx-card__collapsible-content .vx-card__body {
        padding: 0.5rem !important;

    }

    .center-hor {
        text-align: center;
        vertical-align: middle;
        line-height: 4;
        color: white;
    }

    .bg-grid-color {

        text-align: center;
        height: 60px;
        background-color: #545867;
    }

    .bg-grid-color-success {

        text-align: center;
        height: 60px;
        background-color: limegreen;
    }
</style>
