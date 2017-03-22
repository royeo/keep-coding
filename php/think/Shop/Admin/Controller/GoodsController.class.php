<?php
namespace Admin\Controller;
use Think\Controller;
class GoodsController extends Controller
{
	function show()
	{
		// $goods = new \Model\EnglishModel();
		$goods = new \Model\GoodsModel();
		$info = $goods->select();

		$this->assign('info', $info);


		$this->display();
	}

	function add()
	{
		$this->display();
	}

	function update()
	{
		$this->display();
	}
}
?>
