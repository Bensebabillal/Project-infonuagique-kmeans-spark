<template>
    <bottomNavigation :bottomBarArray="bottomBarArray">

    </bottomNavigation>
</template>

<script>
    import bottomNavigation from 'vue-bottom-navigation/src/components/bottomNavigation'


    export default {
        name: "BottomNavBar",
        data() {
            return {
                bottomBarArray: [
                    {
                        imgBlur: require('../../assets/img/material_location_dark.png'),
                        imgSelect: require('../../assets/img/material_location.png'),
                        title: '定位',
                        titleBlurColor: '#757575',
                        titleSelectColor: '#4CAF50'
                    },
                    {
                        imgBlur: require('../../assets/img/material_car_dark.png'),
                        imgSelect: require('../../assets/img/material_car.png'),
                        title: '购物车',
                        titleBlurColor: '#757575',
                        titleSelectColor: '#4CAF50'
                    },
                    {
                        imgBlur: require('../../assets/img/material_time_dark.png'),
                        imgSelect: require('../../assets/img/material_time.png'),
                        title: '时间',
                        titleBlurColor: '#757575',
                        titleSelectColor: '#4CAF50'
                    }
                ]
            }
        },
        components: {
            bottomNavigation,
        },
    }
</script>

<style scoped>
    .a {
        transition: All 0.4s ease-in-out;
        -webkit-transition: All 0.4s ease-in-out;
        -moz-transition: All 0.4s ease-in-out;
        -o-transition: All 0.4s ease-in-out;
        width: 200px;
        height: 100px;
        background-color: #000000;
        display: block;
        margin: 100px auto;
        color: #fff;
        text-align: center;
        line-height: 100px;
        font-size: 10px;
        font-weight: bold;
    }

    .a:active, .a:focus {
        transform: scale(1.2);
        -webkit-transform: scale(1.2);
        -moz-transform: scale(1.2);
        -o-transform: scale(1.2);
        -ms-transform: scale(1.2);
    }
</style>