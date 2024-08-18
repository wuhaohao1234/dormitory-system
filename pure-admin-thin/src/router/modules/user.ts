export default {
  path: "/user",
  redirect: "/user/list",
  meta: {
    icon: "ri:userrmation-line",
    // showLink: false,
    title: "用户",
    rank: 3
  },
  children: [
    {
      path: "/user/list",
      name: "user",
      component: () => import("@/views/user/index.vue"),
      meta: {
        title: "用户列表"
      }
    },
  ]
} satisfies RouteConfigsTable;
