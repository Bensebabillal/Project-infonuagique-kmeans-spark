<!-- =========================================================================================
  File Name: ItemGridView.vue
  Description: Item Component - Grid VIew
  ----------------------------------------------------------------------------------------
  Item Name: Vuexy - Vuejs, HTML & Laravel Admin Dashboard Template
  Author: Pixinvent
  Author URL: http://www.themeforest.net/user/pixinvent
========================================================================================== -->

<template>
    <!-- <div class="item-grid-view vx-row match-height">
        <div class="vx-col" :class="gridColumnWidth" v-for="item in items" :key="item.objectID"> -->
    <vx-card class="grid-view-item mb-base overflow-hidden" v-on="$listeners" style="border-radius: 0.5rem !important;">
        <template slot="no-body">

            <!-- ITEM IMAGE -->
            <div class="item-img-container bg-black-dark h-64 flex items-center justify-center mb-4 cursor-pointer"
                 @click="navigate_to_detail_view">
                <img :src="item.exercises[0].image" :alt="item.name" class="grid-view-img px-4">
            </div>
            <div class="item-details px-4">
                <div class="">
                    <h4 class="truncate font-semibold mb-1 hover:text-primary cursor-pointer"
                        @click="navigate_to_detail_view">{{ item.name }}</h4>
                    <!--                    <p class="item-description truncate text-sm">{{ item.description }}</p>-->
                </div>
                <!-- RATING & PRICE -->
                <div class="flex justify-between items-center">
                    <div class="text-warning flex py-1 px-2 rounded">
                        <vs-chip>
                            <vs-avatar icon="today" color="dark"/>
                            {{item.week}}
                        </vs-chip>
                        <vs-chip>
                            <vs-avatar icon="alarm" color="dark"/>
                            {{item.day_in_week}}
                        </vs-chip>
                        <vs-chip>
                            <vs-avatar icon="brightness_4" color="dark"/>
                            {{item.time_in_day}}
                        </vs-chip>

                    </div>
                    <!--                    <h6 class="font-bold">${{ item.price }}</h6>-->
                </div>

                <!--                 TITLE & DESCRIPTION -->

            </div>

            <!-- SLOT: ACTION BUTTONS -->
            <slot name="action-buttons"/>
        </template>
    </vx-card>
    <!--  </div>
 </div> -->
</template>

<script>

    export default {
        components: {},
        props: {
            item: {
                type: Object,
                required: true
            }
        },
        methods: {
            navigate_to_detail_view() {
                this.$router.push({name: 'training-Session', params: {item_id: 'test'}})
                    .catch(() => {
                    })
            }
        }
    }
</script>

<style lang="scss" scoped>
    .bg-black-dark {
        background-color: black;
    }

    .grid-view-item {
        .grid-view-img {
            max-width: 100%;
            max-height: 100%;
            width: auto;
            transition: .35s;
        }

        .h-64 {
            height: 10rem !important;
        }

        &:hover {
            transform: translateY(-5px);
            box-shadow: 0px 4px 25px 0px rgba(0, 0, 0, .25);

            .grid-view-img {
                opacity: 0.9;
            }
        }
    }
</style>
