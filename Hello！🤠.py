import streamlit as st

st.set_page_config(
    page_title="HELLO",
    page_icon="🚀",
)

gradient_text_html = """
<style>
.gradient-text {
    font-weight: bold;
    background: -webkit-linear-gradient(left,blue,cyan);
    background: linear-gradient(to right,blue,cyan);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 3em;
}
</style>
<div class="gradient-text">欢迎使用 Vulnerability Detector!</div>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)

with st.sidebar:
    st.info("请在上方选择你想要的功能👆")
    st.markdown("<h1 style='text-align: center;'>简介 ⌨️</h1>", unsafe_allow_html=True)
    st.markdown(
        "  这是基于大语言模型并使用Rewarding奖励模型训练的源代码漏洞挖掘检测系统🏆🏆🏆"
    )
    st.markdown(
        "  它可以针对源代码漏洞做许多事情，并为您提供一些提示。"
    )
    st.markdown(
        "  本工具仍在不断开发完善中…… "
    )
    st.markdown("---")
    st.markdown("<h1 style='text-align: center;'> About 💻</h1>", unsafe_allow_html=True)
    st.markdown(
        "  This is a source code vulnerability detection system based on a "
        "large language model and trained using the Rewarding model. 🏆🏆🏆"
    )
    st.markdown(
        "  It can do anything about source code vulnerabilities you asked and give you some tips."
    )
    st.markdown(
        "  This tool is a work in progress... "
    )

st.markdown(
    """
    #### 🎈Vulnerability Detector 是一个基于大语言模型的源代码漏洞检测工具。
    **👈 从侧边栏选择一个演示**，看看 **Vulnerability Detector** 能做什么吧！
    ### 想了解更多吗？
    - 查看 [Vulnerability Detector.io](https://www.baidu.com)
    - 阅读我们的 [文档](https://www.baidu.com)
    - 在我们的 [社区论坛](https://www.baidu.com) 提问
    ### 不知道怎么开始？
    - 使用该网址内提及的一些漏洞，让大模型来分析一下吧！ [这里有许多漏洞 📊](https://blog.csdn.net/Jailman/article/details/85790733)
    ### 🧭 开始你的探索吧~
"""

)


st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 40%;
            background-color: #f0f0f0;
            padding: 10px;
            text-align: center;

        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>注意：本系统可能会犯错误! 考虑检查重要信息!!!</div>", unsafe_allow_html=True)
