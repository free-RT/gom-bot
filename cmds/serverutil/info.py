import discord
from discord.ext import commands


class infomation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_badge = {"UserFlags.verified_bot_developer": "<:verified_bot_developer:991964080292233306>", "UserFlags.early_supporter": "<:early_supporter:991963681502003230>", "UserFlags.staff": "<:discord_staff:991963642729869372>", "UserFlags.partner": "<:partnered_server_owner:991964149884137472>", "UserFlags.hypesquad": "<:discord_HypeSquad_disc:991962182604566639>",
                           "UserFlags.bug_hunter": "<:bug_hunter:991963877770276944>", "UserFlags.hypesquad_bravery": "<:discord_hypesquad_bravery_disc:991962211641741392>", "UserFlags.hypesquad_brilliance": "<:discord_hypesquad_briliance_disc:991962274816331796>", "UserFlags.hypesquad_balance": "<:discord_hypesquad_balance_disc:991962200879157288>"}
        self.bt = "<:discord_Bot_disc:991962236706885734>"
        self.vbt = "<:verified_bot:991963186234413139>"

    @commands.command(
        aliases=["ui", "ユーザー情報"]
    )
    async def userinfo(self, ctx: commands.Context, user: discord.User = None):
        """
        NLang ja ユーザー情報を表示するコマンドです
        ユーザー情報を表示するコマンドです
        **使いかた：**
        EVAL self.bot.command_prefix+'userinfo ユーザーid'
        EVAL self.bot.command_prefix+'userinfo'
        ELang ja
        NLang default Sorry, this command only supports Japanese.
        Sorry, this command only supports Japanese.
        ELang default
        """
        ebds = list()
        if user == None:
            user = ctx.author
        badge = ""
        for flg in user.public_flags.all():
            badge = badge + self.user_badge.get(str(flg), "")
        name = user.name+'#'+user.discriminator
        if user.bot:
            if user.public_flags.verified_bot:
                name = name + self.vbt
            else:
                name = name + self.bt
        ebd = discord.Embed(title=name+'の情報', color=self.bot.Color)
        if badge != "":
            ebd.add_field(name="バッジ", value=badge)
        ebd.add_field(name="ID", value="```" + str(user.id) + "```")
        ebd.add_field(name="アカウント作成日",
                      value=discord.utils.format_dt(user.created_at))
        ebd.add_field(name="アイコンurl", value=user.avatar.url)
        member = ctx.guild.get_member(user.id)
        if member != None:
            if member.guild_avatar != None:
                ebd.add_field(name="このサーバーでのアイコンurl",
                              value=member.guild_avatar.url)
            ebd.add_field(name="表示名", value=member.display_name)
            ebd.add_field(name="サーバーへの参加日",
                          value=discord.utils.format_dt(member.joined_at))
        ebd.set_thumbnail(url=user.avatar.url)
        ebds.append(ebd)
        if member != None:
            send = ""
            user = member
            roles = ""
            for r in user.roles:
                roles = roles + " " + r.mention
            if member.guild_permissions.administrator:
                send = send+':white_check_mark:管理者\n'
            else:
                send = send+':x:管理者\n'
            if user.guild_permissions.ban_members:
                send = send+':white_check_mark:ユーザーをban\n'
            else:
                send = send+':x:ユーザーをban\n'
            if user.guild_permissions.kick_members:
                send = send+':white_check_mark:ユーザーをkick\n'
            else:
                send = send+':x:ユーザーをkick\n'
            if user.guild_permissions.manage_channels:
                send = send+':white_check_mark:チャンネルの管理\n'
            else:
                send = send+':x:チャンネルの管理\n'
            if user.guild_permissions.create_instant_invite:
                send = send+':white_check_mark:招待リンクを作成\n'
            else:
                send = send+':x:招待リンクを作成\n'
            if user.guild_permissions.manage_guild:
                send = send+':white_check_mark:サーバーの管理\n'
            else:
                send = send+':x:サーバーの管理\n'
            if user.guild_permissions.view_audit_log:
                send = send+':white_check_mark:監査ログの表示\n'
            else:
                send = send+':x:監査ログの表示\n'
            if user.guild_permissions.add_reactions:
                send = send+':white_check_mark:リアクションの追加\n'
            else:
                send = send+':x:リアクションの追加\n'
            if user.guild_permissions.priority_speaker:
                send = send+':white_check_mark:優先スピーカー\n'
            else:
                send = send+':x:優先スピーカー\n'
            if user.guild_permissions.stream:
                send = send+':white_check_mark:配信\n'
            else:
                send = send+':x:配信\n'
            if user.guild_permissions.view_channel:
                send = send+':white_check_mark:チャンネルを見る\n'
            else:
                send = send+':x:チャンネルを見る\n'
            if user.guild_permissions.read_message_history:
                send = send+':white_check_mark:メッセージ履歴を読む\n'
            else:
                send = send+':x:メッセージ履歴を読む\n'
            if user.guild_permissions.send_messages:
                send = send+':white_check_mark:メッセージの送信\n'
            else:
                send = send+':x:メッセージの送信\n'
            if user.guild_permissions.send_tts_messages:
                send = send+':white_check_mark:ttsコマンドの使用\n'
            else:
                send = send+':x:ttsコマンドの使用\n'
            if user.guild_permissions.manage_messages:
                send = send+':white_check_mark:メッセージの管理\n'
            else:
                send = send+':x:メッセージの管理\n'
            if user.guild_permissions.embed_links:
                send = send+':white_check_mark:埋め込みリンクを使用\n'
            else:
                send = send+':x:埋め込みリンクを使用\n'
            if user.guild_permissions.attach_files:
                send = send+':white_check_mark:ファイルを送信\n'
            else:
                send = send+':x:ファイルを送信\n'
            if user.guild_permissions.mention_everyone:
                send = send+':white_check_mark:全てのロールにメンション\n'
            else:
                send = send+':x:全てのロールにメンション\n'
            if user.guild_permissions.use_external_emojis:
                send = send+':white_check_mark:外部の絵文字の使用\n'
            else:
                send = send+':x:外部の絵文字の使用\n'
            if user.guild_permissions.use_external_stickers:
                send = send+':white_check_mark:外部のスタンプの使用\n'
            else:
                send = send+':x:外部のスタンプの使用\n'
            if user.guild_permissions.view_guild_insights:
                send = send+':white_check_mark:サーバーインサイトの表示\n'
            else:
                send = send+':x:サーバーインサイトの表示\n'
            if user.guild_permissions.connect:
                send = send+':white_check_mark:ボイスチャンネルに接続\n'
            else:
                send = send+':x:ボイスチャンネルに接続\n'
            if user.guild_permissions.speak:
                send = send+':white_check_mark:ボイスチャンネルで発言\n'
            else:
                send = send+':x:ボイスチャンネルで発言\n'
            if user.guild_permissions.mute_members:
                send = send+':white_check_mark:メンバーをミュート\n'
            else:
                send = send+':x:メンバーをミュート\n'
            if user.guild_permissions.deafen_members:
                send = send+':white_check_mark:メンバーのスピーカーをミュート\n'
            else:
                send = send+':x:メンバーのスピーカーをミュート\n'
            if user.guild_permissions.move_members:
                send = send+':white_check_mark:メンバーの移動\n'
            else:
                send = send+':x:メンバーの移動\n'
            if user.guild_permissions.use_voice_activation:
                send = send+':white_check_mark:音声検出の使用\n'
            else:
                send = send+':x:音声検出の使用\n'
            if user.guild_permissions.change_nickname:
                send = send+':white_check_mark:ニックネームの変更\n'
            else:
                send = send+':x:ニックネームの変更\n'
            if user.guild_permissions.manage_nicknames:
                send = send+':white_check_mark:ニックネームの管理\n'
            else:
                send = send+':x:ニックネームの管理\n'
            if user.guild_permissions.manage_permissions:
                send = send+':white_check_mark:ロールの管理\n'
            else:
                send = send+':x:ロールの管理\n'
            if user.guild_permissions.manage_webhooks:
                send = send+':white_check_mark:ウェブフックの管理\n'
            else:
                send = send+':x:ウェブフックの管理\n'
            if user.guild_permissions.manage_emojis_and_stickers:
                send = send+':white_check_mark:絵文字の管理\n'
            else:
                send = send+':x:絵文字の管理\n'
            if user.guild_permissions.use_application_commands:
                send = send+':white_check_mark:アプリケーションコマンドの使用\n'
            else:
                send = send+':x:アプリケーションコマンドの使用\n'
            if user.guild_permissions.request_to_speak:
                send = send+':white_check_mark:スピーカー参加をリクエスト\n'
            else:
                send = send+':x:スピーカー参加をリクエスト\n'
            if user.guild_permissions.manage_events:
                send = send+':white_check_mark:イベントの管理\n'
            else:
                send = send+':x:イベントの管理\n'
            if user.guild_permissions.manage_threads:
                send = send+':white_check_mark:スレッドの管理\n'
            else:
                send = send+':x:スレッドの管理\n'
            if user.guild_permissions.create_public_threads:
                send = send+':white_check_mark:公開スレッドの作成\n'
            else:
                send = send+':x:公開スレッドの作成\n'
            if user.guild_permissions.create_private_threads:
                send = send+':white_check_mark:非公開スレッドの作成\n'
            else:
                send = send+':x:非公開スレッドの作成\n'
            if user.guild_permissions.send_messages_in_threads:
                send = send+':white_check_mark:スレッドでメッセージを送信\n'
            else:
                send = send+':x:スレッドでメッセージを送信\n'
            perms = discord.Embed(
                title=user.name+'#'+user.discriminator+'の権限', description=send, color=self.bot.Color)
            rls = discord.Embed(title=user.name+'#'+user.discriminator +
                                'のロール', description=roles, color=self.bot.Color)
            ebds.append(rls)
            ebds.append(perms)
        alm = discord.AllowedMentions.none()
        await ctx.send(embeds=ebds, allowed_mentions=alm)


async def setup(bot):
    await bot.add_cog(infomation(bot))
