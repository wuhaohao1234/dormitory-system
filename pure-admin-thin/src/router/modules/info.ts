export default {
  path: "/info",
  redirect: "/info/detail",
  meta: {
    icon: "ri:information-line",
    // showLink: false,
    title: "详情",
    rank: 2
  },
  children: [
    {
      path: "/info/detail",
      name: "detail",
      component: () => import("@/views/info/index.vue"),
      meta: {
        title: "个人信息"
      }
    },
  ]
} satisfies RouteConfigsTable;
