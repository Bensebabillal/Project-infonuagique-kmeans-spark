<!-- =========================================================================================
  File Name: ECommerceShop.vue
  Description: eCommerce Shop Page
  ----------------------------------------------------------------------------------------
  Item Name: Vuexy - Vuejs, HTML & Laravel Admin Dashboard Template
    Author: Pixinvent
  Author URL: http://www.themeforest.net/user/pixinvent
========================================================================================== -->

<template>
    <div>
        <div
                :search-client="searchClient"
                index-name="instant_search" id="algolia-instant-search-demo">


            <div class="algolia-header mb-4">
                <div class="flex md:items-end items-center justify-between flex-wrap">
                    <!-- TOGGLE SIDEBAR BUTTON -->
                    <feather-icon
                            class="inline-flex lg:hidden cursor-pointer mr-4"
                            icon="MenuIcon"
                            @click.stop="toggleFilterSidebar"/>

                    <p class="lg:inline-flex hidden font-semibold algolia-filters-label">Filters</p>

                    <div class="flex justify-between items-end flex-grow">
                        <!-- Stats -->


                        <div class="flex flex-wrap">


                            <!-- ITEM VIEW - GRID/LIST -->
                            <div>
                                <feather-icon
                                        icon="GridIcon"
                                        @click="currentItemView='item-grid-view'"
                                        class="p-2 shadow-drop rounded-lg d-theme-dark-bg cursor-pointer"
                                        :svgClasses="{'text-primary stroke-current': currentItemView == 'item-grid-view'}"/>
                                <feather-icon
                                        icon="ListIcon"
                                        @click="currentItemView='item-list-view'"
                                        class="p-2 ml-4 shadow-drop rounded-lg d-theme-dark-bg cursor-pointer hidden sm:inline-flex"
                                        :svgClasses="{'text-primary stroke-current': currentItemView == 'item-list-view'}"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="algolia-content-container" class="relative clearfix">
                <vs-sidebar
                        class="items-no-padding vs-sidebar-rounded background-absolute"
                        parent="#algolia-content-container"
                        :click-not-close="clickNotClose"
                        :hidden-background="clickNotClose"
                        v-model="isFilterSidebarActive">

                    <div class="p-6 filter-container">

                        <!-- MULTI RANGE -->


                        <!-- CATEGORIES -->
                        <h2 class="font-bold mb-4">Session</h2>

                        <ul>
                            <li v-for="(item,index) in algoliaCategories" :key="index"
                                class="flex items-center cursor-pointer py-1">
                                <feather-icon icon="CircleIcon"
                                              :svgClasses="[{ 'text-primary fill-current': item.isRefined}, 'h-5 w-5']"/>
                                <h5 class="ml-2"
                                    :class="{'text-primary': item.isRefined}">{{ item.value }}</h5>
                            </li>
                        </ul>


                    </div>
                </vs-sidebar>

                <!-- RIGHT COL -->
                <div :class="{'sidebar-spacer-with-margin': clickNotClose}">

                    <!-- SEARCH BAR -->

                    <div class="relative mb-8">


                        <!-- SEARCH LOADING -->
                        <p :hidden="!isSearchStalled" class="mt-4 text-grey">
                            <feather-icon icon="ClockIcon" svgClasses="w-4 h-4" class="mr-2 align-middle"/>
                            <span>Loading...</span>
                        </p>

                        <!-- SEARCH ICON -->
                        <div slot="submit-icon" class="absolute top-0 right-0 py-4 px-6"
                             v-show="!currentRefinement">
                            <feather-icon icon="SearchIcon" svgClasses="h-6 w-6"/>
                        </div>

                        <!-- CLEAR INPUT ICON -->
                        <div slot="reset-icon" class="absolute top-0 right-0 py-4 px-6"
                             v-show="currentRefinement">
                            <feather-icon icon="XIcon" svgClasses="h-6 w-6 cursor-pointer" @click="refine('')"/>
                        </div>
                    </div>


                    <!-- SEARCH RESULT -->
                    <div>
                        <div slot-scope="{ items }">

                            <!-- GRID VIEW -->
                            <template v-if="currentItemView == 'item-grid-view'">
                                <div class="items-grid-view vx-row match-height">
                                    <div class="vx-col lg:w-1/3 sm:w-1/2 w-full" v-for="item in items"
                                         :key="item.objectID">

                                        <item-grid-view :item="item">

                                            <!-- SLOT: ACTION BUTTONS -->
                                            <template slot="action-buttons">
                                                <div class="flex flex-wrap">

                                                    <!-- PRIMARY BUTTON: ADD TO WISH LIST -->
                                                    <div
                                                            class="item-view-primary-action-btn p-3 flex flex-grow items-center justify-center cursor-pointer"
                                                            @click="toggleItemInWishList(item)">
                                                        <feather-icon icon="HeartIcon"
                                                                      :svgClasses="[{'text-danger fill-current' : isInWishList(item.objectID)}, 'h-4 w-4']"/>

                                                        <span class="text-sm font-semibold ml-2">WISHLIST</span>
                                                    </div>

                                                    <!-- SECONDARY BUTTON: ADD-TO/VIEW-IN CART -->
                                                    <div
                                                            class="item-view-secondary-action-btn bg-primary p-3 flex flex-grow items-center justify-center text-white cursor-pointer"
                                                            @click="cartButtonClicked(item)">
                                                        <feather-icon icon="ShoppingBagIcon" svgClasses="h-4 w-4"/>

                                                        <span class="text-sm font-semibold ml-2"
                                                              v-if="isInCart(item.objectID)">VIEW IN CART</span>
                                                        <span class="text-sm font-semibold ml-2"
                                                              v-else>ADD TO CART</span>
                                                    </div>
                                                </div>
                                            </template>
                                        </item-grid-view>

                                    </div>
                                </div>
                            </template>

                            <!-- LIST VIEW -->
                            <template v-else>
                                <div class="items-list-view mb-base" v-for="item in items" :key="item.objectID">

                                    <item-list-view :item="item">

                                        <!-- SLOT: ACTION BUTTONS -->
                                        <template slot="action-buttons">
                                            <div
                                                    class="item-view-primary-action-btn p-3 rounded-lg flex flex-grow items-center justify-center cursor-pointer mb-3"
                                                    @click="toggleItemInWishList(item)">
                                                <feather-icon icon="HeartIcon"
                                                              :svgClasses="[{'text-danger fill-current' : isInWishList(item.objectID)}, 'h-4 w-4']"/>
                                                <span class="text-sm font-semibold ml-2">WISHLIST</span>
                                            </div>
                                            <div
                                                    class="item-view-secondary-action-btn bg-primary p-3 rounded-lg flex flex-grow items-center justify-center text-white cursor-pointer"
                                                    @click="cartButtonClicked(item)">
                                                <feather-icon icon="ShoppingBagIcon" svgClasses="h-4 w-4"/>

                                                <span class="text-sm font-semibold ml-2" v-if="isInCart(item.objectID)">VIEW IN CART</span>
                                                <span class="text-sm font-semibold ml-2" v-else>ADD TO CART</span>
                                            </div>
                                        </template>
                                    </item-list-view>

                                </div>
                            </template>
                        </div>
                    </div>


                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import algoliasearch from 'algoliasearch/lite'

    export default {
        components: {
            ItemGridView: () => import('./components/ItemGridView.vue'),
            ItemListView: () => import('./components/ItemListView.vue'),

        },
        data() {
            return {
                searchClient: algoliasearch(
                    'latency',
                    '6be0576ff61c053d5f9a3225e2a90f76'
                ),
                // Filter Sidebar
                isFilterSidebarActive: true,
                clickNotClose: true,
                currentItemView: 'item-grid-view',

                algoliaCategories: [
                    {value: 'hello', isRefined: true},
                    {value: 'hello', isRefined: false},
                    {value: 'hello', isRefined: false},
                    {value: 'hello', isRefined: false},

                ]
            }
        },
        computed: {
            toValue() {
                return (value, range) => [
                    value.min !== null ? value.min : range.min,
                    value.max !== null ? value.max : range.max
                ]
            },

            // GRID VIEW
            isInCart() {
                return (itemId) => this.$store.getters['eCommerce/isInCart'](itemId)
            },
            isInWishList() {
                return (itemId) => this.$store.getters['eCommerce/isInWishList'](itemId)
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

            // GRID VIEW - ACTIONS
            toggleFilterSidebar() {
                if (this.clickNotClose) return
                this.isFilterSidebarActive = !this.isFilterSidebarActive
            },
            toggleItemInWishList(item) {
                this.$store.dispatch('eCommerce/toggleItemInWishList', item)
            },
            setSidebarWidth() {
                if (this.windowWidth < 992) {
                    this.isFilterSidebarActive = this.clickNotClose = false
                } else {
                    this.isFilterSidebarActive = this.clickNotClose = true
                }
            },


        },
        created() {
            this.setSidebarWidth()
        }
    }

</script>


<style lang="scss">
    #algolia-instant-search-demo {
        .algolia-header {
            .algolia-filters-label {
                width: calc(260px + 2.4rem);
            }
        }

        #algolia-content-container {

            .vs-sidebar {
                position: relative;
                float: left;
            }
        }

        .algolia-search-input-right-aligned-icon {
            padding: 1rem 1.5rem;
        }

        .algolia-price-slider {
            min-width: unset;
        }

        .item-view-primary-action-btn {
            color: #2c2c2c !important;
            background-color: #f6f6f6;
            min-width: 50%;
        }

        .item-view-secondary-action-btn {
            min-width: 50%;
        }
    }

    .theme-dark {
        #algolia-instant-search-demo {
            #algolia-content-container {
                .vs-sidebar {
                    background-color: #10163a;
                }
            }
        }
    }

    @media (min-width: 992px) {
        .vs-sidebar-rounded {
            .vs-sidebar {
                border-radius: .5rem;
            }

            .vs-sidebar--items {
                border-radius: .5rem;
            }
        }
    }

    @media (max-width: 992px) {
        #algolia-content-container {
            .vs-sidebar {
                position: absolute !important;
                float: none !important;
            }
        }
    }

    #dashboard-analytics {
        .greet-user {
            position: relative;

            .decore-left {
                position: absolute;
                left: 0;
                top: 0;
            }

            .decore-right {
                position: absolute;
                right: 0;
                top: 0;
            }
        }

        @media(max-width: 576px) {
            .decore-left, .decore-right {
                width: 140px;
            }
        }
    }
</style>