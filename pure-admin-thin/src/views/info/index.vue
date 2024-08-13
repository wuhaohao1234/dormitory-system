<template>
  <el-form :model="form" label-width="180px">
    <!-- 性别 -->
    <el-form-item label="性别" prop="gender">
      <el-radio-group v-model="form.gender">
        <el-radio label="男">男</el-radio>
        <el-radio label="女">女</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 家乡所在地区 -->
    <el-form-item label="家乡所在地区" prop="hometown">
      <el-radio-group v-model="form.hometown">
        <el-radio label="南方">南方</el-radio>
        <el-radio label="北方">北方</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 星座 -->
    <el-form-item label="星座" prop="constellation">
      <el-input v-model="form.constellation" placeholder="请输入星座"></el-input>
    </el-form-item>

    <!-- 宿舍成员来自 -->
    <el-form-item label="你期待你的宿舍成员都来自哪里" prop="roommateOrigin">
      <el-radio-group v-model="form.roommateOrigin">
        <el-radio label="南方">南方</el-radio>
        <el-radio label="北方">北方</el-radio>
        <el-radio label="南方北方都有">南方北方都有</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 作息时间 -->
    <el-form-item label="你的作息时间" prop="schedule">
      <el-radio-group v-model="form.schedule">
        <el-radio label="通常11点之前睡">通常11点之前睡</el-radio>
        <el-radio label="通常11点之后睡">通常11点之后睡</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 是否抽烟 -->
    <el-form-item label="你是否抽烟" prop="smoking">
      <el-radio-group v-model="form.smoking">
        <el-radio label="是">是</el-radio>
        <el-radio label="否">否</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 生活卫生习惯 -->
    <el-form-item label="你的生活卫生习惯" prop="hygiene">
      <el-radio-group v-model="form.hygiene">
        <el-radio label="A.很高要求，自认为有“洁癖”">A.很高要求，自认为有“洁癖”</el-radio>
        <el-radio label="B.较高，卫生小标兵">B.较高，卫生小标兵</el-radio>
        <el-radio label="C.一般，会定期搞卫生">C.一般，会定期搞卫生</el-radio>
        <el-radio label="D.自认为“佛系星人”，能住就行">D.自认为“佛系星人”，能住就行</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 睡眠质量 -->
    <el-form-item label="你的睡眠质量" prop="sleepQuality">
      <el-input-number v-model="form.sleepQuality" :min="1" :max="5"></el-input-number>
    </el-form-item>

    <!-- 容易引发宿舍矛盾的因素 -->
    <el-form-item label="你认为容易引发宿舍矛盾的最主要因素" prop="conflictReason">
      <el-radio-group v-model="form.conflictReason">
        <el-radio label="A.性格不合">A.性格不合</el-radio>
        <el-radio label="B.作息不一致">B.作息不一致</el-radio>
        <el-radio label="C.卫生习惯不同">C.卫生习惯不同</el-radio>
        <el-radio label="D.消费观不同">D.消费观不同</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 宿舍和谐相处的关键 -->
    <el-form-item label="你认为宿舍能够和谐相处，共同进步的关键在于" prop="harmonyKey">
      <el-radio-group v-model="form.harmonyKey">
        <el-radio label="A.生活中能够互相包容理解">A.生活中能够互相包容理解</el-radio>
        <el-radio label="B.学习上能够互相帮助">B.学习上能够互相帮助</el-radio>
        <el-radio label="C.本身生活习惯相近">C.本身生活习惯相近</el-radio>
        <el-radio label="D.人生观、世界观、价值观相近">D.人生观、世界观、价值观相近</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- MBTI -->
    <el-form-item label="你的MBTI" prop="mbti">
      <el-select v-model="form.mbti" placeholder="请选择">
        <el-option label="ESFJ 执政官" value="ESFJ"></el-option>
        <el-option label="ISFJ 守卫者" value="ISFJ"></el-option>
        <el-option label="ESFP 表演者" value="ESFP"></el-option>
        <el-option label="ENFP 竞选者" value="ENFP"></el-option>
        <el-option label="ISTJ 物流师" value="ISTJ"></el-option>
        <el-option label="ISFP 探险家" value="ISFP"></el-option>
        <el-option label="ENFJ 主人公" value="ENFJ"></el-option>
        <el-option label="ENTP 辩论家" value="ENTP"></el-option>
        <el-option label="ENTJ 指挥官" value="ENTJ"></el-option>
        <el-option label="ESTP 企业家" value="ESTP"></el-option>
        <el-option label="ESTJ 总经理" value="ESTJ"></el-option>
        <el-option label="INTP 逻辑学家" value="INTP"></el-option>
        <el-option label="ISTP 鉴赏家" value="ISTP"></el-option>
        <el-option label="INFP 调停者" value="INFP"></el-option>
        <el-option label="INTJ 建筑师" value="INTJ"></el-option>
        <el-option label="INFJ 提倡者" value="INFJ"></el-option>
      </el-select>
    </el-form-item>

    <!-- 自我性格评价 -->
    <el-form-item label="自我性格评价" prop="personality">
      <el-checkbox-group v-model="form.personality">
        <el-checkbox label="A.外向热情，广交朋友"></el-checkbox>
        <el-checkbox label="B.性格直爽，快人快语"></el-checkbox>
        <el-checkbox label="C.内向温柔，喜好安静"></el-checkbox>
        <el-checkbox label="D.心思细腻，较为敏感"></el-checkbox>
        <el-checkbox label="E.包容大度，善解人意"></el-checkbox>
      </el-checkbox-group>
    </el-form-item>

    <!-- 社交状态 -->
    <el-form-item label="你本人的社交状态" prop="socialStatus">
      <el-radio-group v-model="form.socialStatus">
        <el-radio label="A.社牛型">A.社牛型</el-radio>
        <el-radio label="B.正常型">B.正常型</el-radio>
        <el-radio label="C.社恐型">C.社恐型</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 矛盾处理方式 -->
    <el-form-item label="当与人产生矛盾时，你更倾向于当面沟通解决吗?" prop="conflictResolution">
      <el-radio-group v-model="form.conflictResolution">
        <el-radio label="是">是</el-radio>
        <el-radio label="否">否</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 兴趣爱好偏向 -->
    <el-form-item label="你的兴趣爱好偏向" prop="hobbies">
      <el-radio-group v-model="form.hobbies">
        <el-radio label="偏静型（读书，绘画等）">偏静型（读书，绘画等）</el-radio>
        <el-radio label="偏动型（运动，游戏等）">偏动型（运动，游戏等）</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 是否玩网络游戏 -->
    <el-form-item label="你是否玩网络游戏" prop="gaming">
      <el-radio-group v-model="form.gaming">
        <el-radio label="是">是</el-radio>
        <el-radio label="否">否</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 毕业之后的打算 -->
    <el-form-item label="毕业之后的打算" prop="postGraduationPlan">
      <el-radio-group v-model="form.postGraduationPlan">
        <el-radio label="A.利用大学时间找到自己的优势，为日后就业做准备">
          A.利用大学时间找到自己的优势，为日后就业做准备
        </el-radio>
        <el-radio label="B.有创业梦想">B.有创业梦想</el-radio>
        <el-radio label="C.打算进一步深造，考取研究生">C.打算进一步深造，考取研究生</el-radio>
        <el-radio label="D.考取公务员或进入国企央企，毕业就有一个相对稳定的工作">
          D.考取公务员或进入国企央企，毕业就有一个相对稳定的工作
        </el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 入学后最想做的三件事 -->
    <el-form-item label="入学后，选出三件你最想做的事情" prop="entryGoals">
      <el-checkbox-group v-model="form.entryGoals">
        <el-checkbox label="A.参与学生工作，竞选班委，学生会，锻炼自己的组织领导能力">
          A.参与学生工作，竞选班委，学生会，锻炼自己的组织领导能力
        </el-checkbox>
        <el-checkbox label="B.加入1-2个感兴趣的社团，结交朋友">
          B.加入1-2个感兴趣的社团，结交朋友
        </el-checkbox>
        <el-checkbox label="C.努力提高成绩，提高专业技能">
          C.努力提高成绩，提高专业技能
        </el-checkbox>
        <el-checkbox label="D.考取相关证书（四六级，计算机，普通话）">
          D.考取相关证书（四六级，计算机，普通话）
        </el-checkbox>
        <el-checkbox label="E.利用寒暑假实习，参加社会实践">
          E.利用寒暑假实习，参加社会实践
        </el-checkbox>
        <el-checkbox label="F.了解学校相关政策，包括所修学分要求">
          F.了解学校相关政策，包括所修学分要求
        </el-checkbox>
        <el-checkbox label="G.看看自己是否喜欢本专业，如果不喜欢打算转专业">
          G.看看自己是否喜欢本专业，如果不喜欢打算转专业
        </el-checkbox>
      </el-checkbox-group>
    </el-form-item>

    <!-- 大学期间最希望自己成为什么样的人 -->
    <el-form-item label="大学期间，你最希望自己能够成为一个什么样的人" prop="universityGoal">
      <el-radio-group v-model="form.universityGoal">
        <el-radio label="A.学霸型">A.学霸型</el-radio>
        <el-radio label="B.生活小能手">B.生活小能手</el-radio>
        <el-radio label="C.社交达人">C.社交达人</el-radio>
        <el-radio label="D.优秀志愿服务者">D.优秀志愿服务者</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 最期待在哪方面进步 -->
    <el-form-item label="在大学期间，你最期待自己在哪方面能够更进一步" prop="progressArea">
      <el-radio-group v-model="form.progressArea">
        <el-radio label="A.学业水平能力">A.学业水平能力</el-radio>
        <el-radio label="B.独立生活能力">B.独立生活能力</el-radio>
        <el-radio label="C.语言表达能力">C.语言表达能力</el-radio>
        <el-radio label="D.人际交往能力">D.人际交往能力</el-radio>
        <el-radio label="E.解决问题能力">E.解决问题能力</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 是否担任过班委 -->
    <el-form-item label="在高中阶段是否担任过班委" prop="classCommittee">
      <el-radio-group v-model="form.classCommittee.status">
        <el-radio label="否">否</el-radio>
        <el-radio label="是">是</el-radio>
      </el-radio-group>
      <el-input
        v-if="form.classCommittee.status === '是'"
        v-model="form.classCommittee.position"
        placeholder="填写职位"
      ></el-input>
    </el-form-item>

    <!-- 寝室整体休息状态 -->
    <el-form-item label="你希望寝室整体的休息状态" prop="roomRestStatus">
      <el-radio-group v-model="form.roomRestStatus">
        <el-radio label="早睡早起">早睡早起</el-radio>
        <el-radio label="晚睡晚起">晚睡晚起</el-radio>
        <el-radio label="早睡晚起">早睡晚起</el-radio>
        <el-radio label="晚睡早起">晚睡早起</el-radio>
        <el-radio label="无所谓">无所谓</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 是否介意室友抽烟 -->
    <el-form-item label="你是否介意你的室友抽烟" prop="smokingRoommate">
      <el-radio-group v-model="form.smokingRoommate">
        <el-radio label="介意">介意</el-radio>
        <el-radio label="不介意">不介意</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 寝室卫生看法 -->
    <el-form-item label="关于寝室卫生你如何看待" prop="roomHygiene">
      <el-radio-group v-model="form.roomHygiene">
        <el-radio label="A.非常在意寝室的卫生情况，有洁癖">
          A.非常在意寝室的卫生情况，有洁癖
        </el-radio>
        <el-radio label="B.和室友商议协定，定期打扫卫生">
          B.和室友商议协定，定期打扫卫生
        </el-radio>
        <el-radio label="C.偶尔和室友打扫">C.偶尔和室友打扫</el-radio>
        <el-radio label="D.只顾个人区域，他人卫生无暇顾及">
          D.只顾个人区域，他人卫生无暇顾及
        </el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 是否介意与高年级混住 -->
    <el-form-item label="你是否介意和高年级的学长或学姐混住" prop="mixedYearRoommates">
      <el-input-number v-model="form.mixedYearRoommates" :min="1" :max="5"></el-input-number>
    </el-form-item>

    <!-- 是否介意室友唱歌或外放打电话 -->
    <el-form-item
      label="你是否介意你的室友在宿舍大声唱歌，休息的时间外放打电话"
      prop="noiseTolerance"
    >
      <el-input-number v-model="form.noiseTolerance" :min="1" :max="5"></el-input-number>
    </el-form-item>

    <!-- 希望室友来自同一地区还是不同地区 -->
    <el-form-item
      label="你更希望自己的舍友们是来自不同省市的还是同一地区"
      prop="roommateRegion"
    >
      <el-radio-group v-model="form.roommateRegion">
        <el-radio label="A.不同地区">A.不同地区</el-radio>
        <el-radio label="B.同一地区">B.同一地区</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 希望E人同寝还是I人同寝 -->
    <el-form-item label="你希望和E人（外向型）还是I人（内向型）同寝" prop="extravertIntrovert">
      <el-radio-group v-model="form.extravertIntrovert">
        <el-radio label="全部E人">全部E人</el-radio>
        <el-radio label="全部I人">全部I人</el-radio>
        <el-radio label="E人和I人混合">E人和I人混合</el-radio>
      </el-radio-group>
    </el-form-item>

    <!-- 看重的因素 -->
    <el-form-item label="你认为选择室友你更看重哪个因素" prop="importantFactor">
      <el-select v-model="form.importantFactor" placeholder="请选择">
        <el-option
          v-for="(option, index) in importantFactors"
          :key="index"
          :label="option.label"
          :value="option.value"
        ></el-option>
      </el-select>
    </el-form-item>

    <!-- 提交按钮 -->
    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { reactive, ref } from "vue";
import { ElMessage } from "element-plus";

// 表单数据
const form = ref({
  gender: "",
  hometown: "",
  constellation: "",
  roommateOrigin: "",
  schedule: "",
  smoking: "",
  hygiene: "",
  sleepQuality: null,
  conflictReason: "",
  harmonyKey: "",
  mbti: "",
  personality: [],
  socialStatus: "",
  conflictResolution: "",
  hobbies: "",
  gaming: "",
  postGraduationPlan: "",
  entryGoals: [],
  universityGoal: "",
  progressArea: "",
  classCommittee: {
    status: "",
    position: ""
  },
  roomRestStatus: "",
  smokingRoommate: "",
  roomHygiene: "",
  mixedYearRoommates: null,
  noiseTolerance: null,
  roommateRegion: "",
  extravertIntrovert: "",
  importantFactor: ""
});

// 可选的“看重因素”
const importantFactors = [
  { label: "性格", value: "性格" },
  { label: "生活习惯", value: "生活习惯" },
  { label: "兴趣爱好", value: "兴趣爱好" },
  { label: "作息时间", value: "作息时间" }
];

// 表单验证
const formRef = ref(null);

const onSubmit = () => {
  console.log(form.value);
};
</script>

<style scoped>
/* 可以根据需要自定义样式 */
</style>
