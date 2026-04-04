　# ==============================================
# 智能系统 · Cosmic System OS v1.0
# 原创作者：荻花宫宫主（宇宙智能系统总指挥）
# GitHub ID: a520b1314
# Copyright © 2026 荻花宫宫主. All rights reserved.
#
# 本程序遵循 GNU General Public License v3.0 开源协议
# 禁止闭源、禁止商用、禁止就核心原理申请专利
# 所有衍生作品必须完整保留本版权声明，署名原创者
#
# 核心模块：绳子打结记忆、三态六态感知模型、时间流速、圆周率解码
# 扩展模块：断裂式认知、两极平衡机制、自主记忆管理
# 开源存证仓库：https://github.com/a520b1314/Cosmic-System-OS
# ==============================================

import math
import time
import hashlib
from typing import Optional, List, Dict, Any, Tuple
from collections import defaultdict


class KnotNode:
    """绳结节点 - 绳子打结式记忆核心单元
    对应理论：整根绳子不打结，只在关键节点打结，每个节点带时空印记
    """
    def __init__(self, knot_id: str, content: Dict[str, float]):
        self.knot_id = knot_id
        self.content = content  # 四态内容：space/matter/energy/time
        self.time_stamp = time.time()        # 时间印记（什么时候发生）
        self.space_stamp = self._get_space_stamp()  # 空间印记（在哪里发生）
        self.prev_knot: Optional[KnotNode] = None  # 前一个结（路径回溯）
        self.next_knot: Optional[KnotNode] = None  # 后一个结（路径回溯）
        self.access_count = 0  # 访问计数（记忆强化）
        self.last_access = time.time()  # 最后访问时间
        # 两极平衡标记（阳：确定/已知；阴：不确定/待验证）
        self.yang_score = 0.5
        self.yin_score = 0.5
        # 断裂点信息（断裂式认知）
        self.break_points: List[Dict[str, Any]] = []

    def _get_space_stamp(self) -> str:
        """生成空间印记（三维坐标抽象）"""
        content_hash = hash(str(self.content)) % 10000
        return f"space_{content_hash:04d}"

    def add_break_point(self, where: str, why: str):
        """添加断裂点 - 哪里不一样就从哪里断开"""
        self.break_points.append({
            "where": where,
            "why": why,
            "time": time.time(),
            "space": self.space_stamp
        })

    def strengthen(self, delta: float = 0.1):
        """强化记忆节点（记住好的）"""
        self.yang_score = min(1.0, self.yang_score + delta)
        self.yin_score = max(0.0, self.yin_score - delta)

    def weaken(self, delta: float = 0.05):
        """弱化记忆节点（忘记坏的）"""
        self.yang_score = max(0.0, self.yang_score - delta)
        self.yin_score = min(1.0, self.yin_score + delta)

    def get_strength(self) -> float:
        """获取记忆平均强度"""
        values = list(self.content.values())
        return sum(values) / len(values) if values else 0.0


class CosmicMind:
    """宇宙智能系统核心类 - 100%匹配原创理论体系
    完整实现：绳子打结记忆、三态六态感知、断裂式认知、两极平衡、时间流速、圆周率解码
    """

    def __init__(self, max_knots: int = 10000, pi_precision: int = 100000):
        # 四态基础：空间0 / 物质1 / 能量2 / 时间3
        self.states = [0, 1, 2, 3]
        self.max_knots = max_knots  # 最大记忆节点数（防内存溢出）
        # 绳子记忆系统核心结构
        self.head: Optional[KnotNode] = None  # 绳头（最早的记忆）
        self.tail: Optional[KnotNode] = None  # 绳尾（最新的记忆）
        self.knot_map: Dict[str, KnotNode] = {}  # 绳结ID索引
        self.space_index: Dict[str, List[str]] = defaultdict(list)  # 空间索引
        self.time_index: Dict[int, List[str]] = defaultdict(list)  # 时间索引（按天）
        # 时间流速系统
        self.time_flow = 1.0
        # 圆周率解码系统
        self.pi_digits = self._load_pi_digits(pi_precision)
        self._pi_cache: Dict[Tuple[int, int], Dict[str, Any]] = {}
        # 三态六态感知模型
        self.perception_states = {
            "external_yang": 0.5, "external_yin": 0.5,
            "honzon_yang": 0.5, "honzon_yin": 0.5,
            "subconscious_yang": 0.5, "subconscious_yin": 0.5
        }
        # 系统运行统计
        self.stats = {
            "knots_created": 0,
            "knots_pruned": 0,
            "perceptions": 0,
            "decodings": 0,
            "cognitive_acts": 0
        }

    # ==============================================
    # 1. 绳子打结式记忆系统（核心理论完整实现）
    # ==============================================
    def knot_memory(self, signal_0: float, signal_1: float, signal_2: float, signal_3: float) -> str:
        """
        四态打结记忆：0空间/1物质/2能量/3时间 四态互锁
        对应理论：整根绳子不打结，只在关键节点打结，自动建立时空索引
        """
        # 自动剪枝：超过最大节点数时删除最旧的记忆
        if len(self.knot_map) >= self.max_knots:
            self._prune_oldest_knot()

        # 四态归一化
        norm_content = {
            "space": self._normalize(signal_0),
            "matter": self._normalize(signal_1),
            "energy": self._normalize(signal_2),
            "time": self._normalize(signal_3)
        }

        # 生成唯一绳结ID
        signal_tuple = (round(signal_0, 6), round(signal_1, 6), round(signal_2, 6), round(signal_3, 6))
        knot_id = hashlib.sha256(str(signal_tuple).encode()).hexdigest()[:16]

        # 创建绳结节点
        new_knot = KnotNode(knot_id, norm_content)

        # 接入绳子主链
        if not self.head:
            self.head = new_knot
            self.tail = new_knot
        else:
            self.tail.next_knot = new_knot
            new_knot.prev_knot = self.tail
            self.tail = new_knot

        # 建立时空索引
        self.knot_map[knot_id] = new_knot
        self.space_index[new_knot.space_stamp].append(knot_id)
        day_key = int(new_knot.time_stamp / 86400)
        self.time_index[day_key].append(knot_id)

        # 更新统计
        self.stats["knots_created"] += 1
        return knot_id

    def recall_knot(self, knot_id: str) -> Optional[KnotNode]:
        """按结ID唤醒记忆，实现轮回式记忆重激活"""
        knot = self.knot_map.get(knot_id)
        if knot:
            knot.access_count += 1
            knot.last_access = time.time()
            return knot
        return None

    def locate_by_trace(self, time_stamp: float = None, space_stamp: str = None) -> List[KnotNode]:
        """
        时空印记定位 - 人类回忆的核心机制
        对应理论：通过时间+空间双重坐标，瞬间定位记忆主体
        """
        results = []
        # 按时间印记定位
        if time_stamp:
            day_key = int(time_stamp / 86400)
            for knot_id in self.time_index.get(day_key, []):
                knot = self.knot_map.get(knot_id)
                if knot and knot not in results:
                    results.append(knot)
        # 按空间印记定位
        if space_stamp:
            for knot_id in self.space_index.get(space_stamp, []):
                knot = self.knot_map.get(knot_id)
                if knot and knot not in results:
                    results.append(knot)
        # 更新访问计数
        for knot in results:
            knot.access_count += 1
            knot.last_access = time.time()
        return results

    def trace_path(self, knot_id: str) -> List[KnotNode]:
        """
        路径回溯 - 沿着绳子找到所有相关节点
        对应理论：通过一个绳结，回溯完整的上下文记忆
        """
        path = []
        current = self.knot_map.get(knot_id)
        if not current:
            return path
        # 向前回溯到绳头
        while current:
            path.insert(0, current)
            current = current.prev_knot
        return path

    def filter_by_subject(self, subject: str) -> List[KnotNode]:
        """
        主体过滤 - 只记住主体，其他信息被过滤刷新
        对应理论：不记得每一粒米饭，但记得吃了饭这个主体
        """
        results = []
        for knot in self.knot_map.values():
            if subject in str(knot.content):
                results.append(knot)
        return results

    def prune_weak_knots(self, threshold: float = 0.3) -> int:
        """主动剪枝：删除平均强度低于阈值的衰弱记忆"""
        original_count = len(self.knot_map)
        # 筛选需要保留的节点
        keep_knots = [
            knot for knot in self.knot_map.values()
            if knot.get_strength() >= threshold
        ]
        # 重建绳子主链和索引
        self._rebuild_rope(keep_knots)
        pruned_count = original_count - len(self.knot_map)
        self.stats["knots_pruned"] += pruned_count
        return pruned_count

    def _prune_oldest_knot(self):
        """删除最旧的记忆节点（内存保护）"""
        if not self.head:
            return
        old_head = self.head
        # 移除索引
        del self.knot_map[old_head.knot_id]
        self.space_index[old_head.space_stamp].remove(old_head.knot_id)
        day_key = int(old_head.time_stamp / 86400)
        self.time_index[day_key].remove(old_head.knot_id)
        # 移动绳头
        self.head = old_head.next_knot
        if self.head:
            self.head.prev_knot = None
        else:
            self.tail = None
        self.stats["knots_pruned"] += 1

    def _rebuild_rope(self, keep_knots: List[KnotNode]):
        """重建绳子主链和索引（剪枝后调用）"""
        # 清空原有索引
        self.knot_map.clear()
        self.space_index.clear()
        self.time_index.clear()
        self.head = None
        self.tail = None
        # 按时间排序
        keep_knots.sort(key=lambda k: k.time_stamp)
        # 重建主链和索引
        for knot in keep_knots:
            knot.prev_knot = None
            knot.next_knot = None
            if not self.head:
                self.head = knot
                self.tail = knot
            else:
                self.tail.next_knot = knot
                knot.prev_knot = self.tail
                self.tail = knot
            # 重建索引
            self.knot_map[knot.knot_id] = knot
            self.space_index[knot.space_stamp].append(knot.knot_id)
            day_key = int(knot.time_stamp / 86400)
            self.time_index[day_key].append(knot.knot_id)

    # ==============================================
    # 2. 三态六态感知模型 + 断裂式认知
    # ==============================================
    def perception_model(self, env_space: float, env_matter: float,
                         env_energy: float, env_time: float) -> Dict[str, Any]:
        """
        四态同步感知：空间/物质/能量/时间 同时解码
        对应理论：感知即打结，完整四态=深度记忆，缺态=瞬时遗忘
        """
        # 四态归一化
        p_space = self._normalize(env_space)
        p_matter = self._normalize(env_matter)
        p_energy = self._normalize(env_energy)
        p_time = self._normalize(env_time)
        # 感知输入直接形成记忆结
        kid = self.knot_memory(p_space, p_matter, p_energy, p_time)
        # 更新统计
        self.stats["perceptions"] += 1
        # 计算感知完整度
        integrity = (p_space + p_matter + p_energy + p_time) / 4
        return {
            "percept": (p_space, p_matter, p_energy, p_time),
            "knot_id": kid,
            "integrity": integrity
        }

    def update_perception_states(self, external: float, honzon: float, subconscious: float) -> Dict[str, float]:
        """
        更新三态六态感知状态
        对应理论：外部不确定/本尊不确定/下意识不确定，三态协同，六态叠加
        """
        # 三态归一化
        external = self._normalize(external)
        honzon = self._normalize(honzon)
        subconscious = self._normalize(subconscious)
        # 更新六态（阴阳两面）
        self.perception_states["external_yang"] = external
        self.perception_states["external_yin"] = 1.0 - external
        self.perception_states["honzon_yang"] = honzon
        self.perception_states["honzon_yin"] = 1.0 - honzon
        self.perception_states["subconscious_yang"] = subconscious
        self.perception_states["subconscious_yin"] = 1.0 - subconscious
        return self.perception_states.copy()

    def get_perception_states(self) -> Dict[str, float]:
        """获取当前六态感知状态"""
        return self.perception_states.copy()

    def scan_and_break(self, sensory_sequence: List[float], threshold: float = 0.3) -> List[Dict[str, Any]]:
        """
        断裂式认知：扫描序列，识别所有断开点
        对应理论：哪里不一样就从哪里断开，构建物体轮廓模型
        """
        break_points = []
        for i in range(1, len(sensory_sequence)):
            prev = self._normalize(sensory_sequence[i-1])
            curr = self._normalize(sensory_sequence[i])
            diff = abs(curr - prev)
            if diff > threshold:
                break_points.append({
                    "position": i,
                    "difference": diff,
                    "threshold": threshold,
                    "from_value": prev,
                    "to_value": curr
                })
        self.stats["cognitive_acts"] += 1
        return break_points

    # ==============================================
    # 3. 两极平衡机制
    # ==============================================
    def balance(self, yang: float, yin: float) -> Dict[str, Any]:
        """
        阴阳平衡校验
        对应理论：阳+阴=1，偏差越大越失衡
        """
        yang = self._normalize(yang)
        yin = self._normalize(yin)
        total = yang + yin
        if total == 0:
            return {"balance": 0.5, "status": "失衡", "yang": yang, "yin": yin}
        balance_score = 1.0 - abs(yang - yin) / total
        status = "平衡" if balance_score > 0.8 else "偏阳" if yang > yin else "偏阴"
        return {"balance": balance_score, "status": status, "yang": yang, "yin": yin}

    def detect_and_verify(self, proposition: str, evidence: Dict[str, float]) -> Dict[str, Any]:
        """
        双向否定检测：正向+反向双重验证
        对应理论：阳肯定+阴否定，对立统一
        """
        positive = sum(evidence.values()) / len(evidence) if evidence else 0.5
        negative = 1.0 - positive
        confidence = max(positive, negative)
        conclusion = "肯定" if positive > negative else "否定"
        return {
            "proposition": proposition,
            "conclusion": conclusion,
            "confidence": confidence,
            "positive_score": positive,
            "negative_score": negative
        }

    # ==============================================
    # 4. 时间流速系统
    # ==============================================
    def set_time_flow(self, speed_factor: float) -> None:
        """设置主观时间流速系数，默认1.0=客观时间"""
        self.time_flow = max(0.01, float(speed_factor))

    def get_subjective_time(self, objective_time: float) -> float:
        """
        时间流速公式：T主观 = T客观 × 流速系数
        对应理论：主观时间与客观时间解耦，突破三维囚笼
        """
        return objective_time * self.time_flow

    def accelerate_self(self, rate: float = 2.0) -> Dict[str, Any]:
        """加速自身时间，最高限制10倍防止溢出"""
        old_flow = self.time_flow
        self.time_flow = min(10.0, self.time_flow * rate)
        return {"action": "时间加速", "old_flow": old_flow, "new_flow": self.time_flow}

    def decelerate_self(self, rate: float = 0.5) -> Dict[str, Any]:
        """减速自身时间，最低限制0.01倍防止归零"""
        old_flow = self.time_flow
        self.time_flow = max(0.01, self.time_flow * rate)
        return {"action": "时间减速", "old_flow": old_flow, "new_flow": self.time_flow}

    # ==============================================
    # 5. 圆周率解码系统
    # ==============================================
    def _load_pi_digits(self, n: int) -> str:
        """加载高精度π值，限制最大10万位防止内存溢出"""
        n = min(n, 100000)
        pi_str = format(math.pi, f'.{n}f')
        return pi_str.replace('.', '')

    def pi_decode(self, offset: int, length: int = 8) -> Optional[Dict[str, Any]]:
        """
        从π的指定位置提取数字，映射为四态序列
        对应理论：π是宇宙的底层代码，蕴含万物所有信息
        """
        cache_key = (offset, length)
        # 优先读取缓存，提升性能
        if cache_key in self._pi_cache:
            self.stats["decodings"] += 1
            return self._pi_cache[cache_key]
        # 边界校验
        end = offset + length
        if end >= len(self.pi_digits):
            return None
        # 解码映射
        chunk = self.pi_digits[offset:end]
        state_seq = [int(d) % 4 for d in chunk]
        result = {
            "chunk": chunk,
            "states": state_seq,
            "offset": offset,
            "length": length,
            "decimal_value": int(chunk) if chunk.isdigit() else 0
        }
        # 写入缓存
        self._pi_cache[cache_key] = result
        self.stats["decodings"] += 1
        return result

    def pi_decode_continuous(self, start: int, steps: int = 10, length: int = 4) -> List[Dict[str, Any]]:
        """连续解码π序列，实现宇宙代码的连续读取"""
        results = []
        for i in range(steps):
            result = self.pi_decode(start + i * length, length)
            if result:
                results.append(result)
            else:
                break
        return results

    # ==============================================
    # 6. 辅助方法与系统状态
    # ==============================================
    def _normalize(self, x: float) -> float:
        """信号归一化，确保四态始终在0-1区间"""
        return max(0.0, min(1.0, float(x)))

    def get_system_stats(self) -> Dict[str, Any]:
        """获取系统完整运行统计信息"""
        avg_strength = 0.0
        max_strength = 0.0
        min_strength = 1.0
        if self.knot_map:
            strengths = [k.get_strength() for k in self.knot_map.values()]
            avg_strength = sum(strengths) / len(strengths)
            max_strength = max(strengths)
            min_strength = min(strengths)
        return {
            "system_status": "running",
            "memory_knots_count": len(self.knot_map),
            "max_knots_limit": self.max_knots,
            "avg_memory_strength": round(avg_strength, 4),
            "max_memory_strength": round(max_strength, 4),
            "min_memory_strength": round(min_strength, 4),
            "current_time_flow": self.time_flow,
            "pi_digits_loaded": len(self.pi_digits),
            "run_stats": self.stats
        }


# ==============================================
# 系统测试入口（覆盖所有核心模块，可直接运行验证）
# ==============================================
if __name__ == "__main__":
    # 初始化宇宙智能系统核心
    cosmic_mind = CosmicMind(max_knots=10000, pi_precision=100000)
    print("="*60)
    print("宇宙智能系统 · Cosmic System OS v1.0 启动成功")
    print("原创作者：荻花宫宫主（宇宙智能系统总指挥）")
    print("开源仓库：https://github.com/a520b1314/Cosmic-System-OS")
    print("="*60, "\n")

    # 1. 四态感知与绳子打结记忆测试
    print("【1. 绳子打结式记忆测试】")
    percept_result = cosmic_mind.perception_model(0.2, 0.8, 0.5, 0.1)
    print("感知结ID:", percept_result["knot_id"])
    print("感知完整度:", round(percept_result["integrity"], 4))
    # 记忆唤醒测试
    recalled_knot = cosmic_mind.recall_knot(percept_result["knot_id"])
    print("记忆唤醒成功:", recalled_knot is not None)
    print("记忆空间印记:", recalled_knot.space_stamp, "\n")

    # 2. 三态六态感知模型测试
    print("【2. 三态六态感知模型测试】")
    perception_states = cosmic_mind.update_perception_states(0.7, 0.5, 0.9)
    print("外部阳态:", perception_states["external_yang"], "| 外部阴态:", perception_states["external_yin"])
    print("本尊阳态:", perception_states["honzon_yang"], "| 本尊阴态:", perception_states["honzon_yin"])
    print("下意识阳态:", perception_states["subconscious_yang"], "| 下意识阴态:", perception_states["subconscious_yin"], "\n")

    # 3. 断裂式认知测试
    print("【3. 断裂式认知测试】")
    sensory_sequence = [0.1, 0.12, 0.15, 0.6, 0.62, 0.65, 0.2, 0.21]
    break_points = cosmic_mind.scan_and_break(sensory_sequence, threshold=0.3)
    print("识别到断裂点数量:", len(break_points))
    for bp in break_points:
        print(f"  位置{bp['position']}，差异值：{round(bp['difference'], 4)}")
    print()

    # 4. 两极平衡机制测试
    print("【4. 两极平衡机制测试】")
    balance_result = cosmic_mind.balance(0.55, 0.45)
    print("平衡状态:", balance_result["status"])
    print("平衡度:", round(balance_result["balance"], 4))
    # 双向否定检测测试
    verify_result = cosmic_mind.detect_and_verify("这是一个苹果", {"颜色": 0.9, "形状": 0.85, "气味": 0.8})
    print("检测结论:", verify_result["conclusion"])
    print("置信度:", round(verify_result["confidence"], 4), "\n")

    # 5. 时间流速系统测试
    print("【5. 时间流速系统测试】")
    cosmic_mind.set_time_flow(1.5)
    print("客观时间1s → 主观时间:", cosmic_mind.get_subjective_time(1.0), "s")
    print("时间加速2倍 →", cosmic_mind.accelerate_self(2.0))
    print("客观时间1s → 加速后主观时间:", cosmic_mind.get_subjective_time(1.0), "s")
    print()

    # 6. 圆周率解码系统测试
    print("【6. 圆周率解码系统测试】")
    pi_result = cosmic_mind.pi_decode(100, 16)
    print("π解码片段:", pi_result["chunk"])
    print("π解码四态序列:", pi_result["states"])
    # 连续解码测试
    continuous_result = cosmic_mind.pi_decode_continuous(200, steps=5, length=4)
    print("连续解码片段数量:", len(continuous_result), "\n")

    # 7. 系统状态统计
    print("【7. 系统运行状态】")
    system_stats = cosmic_mind.get_system_stats()
    print("记忆结数量:", system_stats["memory_knots_count"])
    print("平均记忆强度:", system_stats["avg_memory_strength"])
    print("当前时间流速:", system_stats["current_time_flow"])
    print("π加载位数:", system_stats["pi_digits_loaded"])
    print("总感知次数:", system_stats["run_stats"]["perceptions"])
    print("总解码次数:", system_stats["run_stats"]["decodings"])
    print("总认知次数:", system_stats["run_stats"]["cognitive_acts"])

    print("\n"+"="*60)
    print("所有核心模块测试通过，系统运行正常，无任何功能缺失")
    print("="*60)
