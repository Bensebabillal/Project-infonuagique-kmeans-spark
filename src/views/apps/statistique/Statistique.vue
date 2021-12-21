<template>
  <div id="dashboard-analytics">
    <div class="vx-row">

      <div class="vx-col mr-auto ml-auto mt-10 w-full  mb-base">
        <vx-card class="p-2 mt-5" style="border-radius: 15px">
          <iframe style="width:100%;height:200vh;"
                  src="http://127.0.0.1:5500/test.html" title="description"></iframe>
        </vx-card>
      </div>


    </div>


  </div>
</template>
<script>
import VueApexCharts from 'vue-apexcharts'
import {VclFacebook} from 'vue-content-loading'
import {getAPI} from '@/axios'

export default {

  data() {
    return {
      loaded: false,
      themeColors: ['#28C76F', '#28C76F', '#EA5455', '#FF9F43', '#1E1E1E'],
      training_type: [],
      radarChart: {
        series: [{
          name: 'Series 1',
          data: [3, 4, 4, 5, 5, 4, 4],
        }],
        chartOptions: {
          colors: ['#28C76F', '#28C76F', '#EA5455', '#FF9F43', '#1E1E1E'],
          labels: ['Conditioning', 'Speed', 'Endurance', 'Soccer Basics', 'Technique', 'Tactical', 'Mental'],

        }
      },
      card_bg_img_1: require('@/assets/images/pages/card-bg-image-demo-1.jpg'),
      card_bg_img_2: require('@/assets/images/pages/card-bg-image-demo-2.jpg')
    }
  },
  components: {},
  computed: {
    activeUserInfo() {
      return this.$store.state.AppActiveUser
    },
  },
  methods: {},
  // created() {
  //     this.getProgram()
  // },
  mounted() {


  },

}
</script>

<style lang="scss">
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

svg#freepik_stories-missed-chances:not(.animated) .animable {
  opacity: 0;
}

svg#freepik_stories-missed-chances.animated #freepik--Grass--inject-27 {
  animation: 1.5s Infinite linear floating;
  animation-delay: 0s;
}

svg#freepik_stories-missed-chances.animated #freepik--Shadows--inject-27 {
  animation: 1.5s Infinite linear floating;
  animation-delay: 0s;
}

svg#freepik_stories-missed-chances.animated #freepik--Clouds--inject-27 {
  animation: 1.5s Infinite linear floating;
  animation-delay: 1s;
}

svg#freepik_stories-missed-chances.animated #freepik--Goal--inject-27 {
  animation: 1.5s Infinite linear floating;
  animation-delay: 0s;
}

svg#freepik_stories-missed-chances.animated #freepik--soccer-ball--inject-27 {
  animation: 1.5s Infinite linear floating;
  animation-delay: 0s;
}

svg#freepik_stories-missed-chances.animated #freepik--character-2--inject-27 {
  animation: 1.5s Infinite linear floating;
  animation-delay: 0s;
}

svg#freepik_stories-missed-chances.animated #freepik--character-1--inject-27 {
  animation: 1.5s Infinite linear floating;
  animation-delay: 0s;
}

@keyframes floating {
  0% {
    opacity: 1;
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}
</style>
